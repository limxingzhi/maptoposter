"""
HTTP server for the City Map Poster Generator.

Provides a simple REST API to generate map poster images.

Usage:
    uvicorn server:app --host 0.0.0.0 --port 8000

Endpoints:
    GET /poster  - Generate a map poster image
    GET /themes  - List available themes
    GET /docs    - Interactive API documentation (Swagger UI)
"""

from typing import Literal, Optional

from fastapi import FastAPI, Query
from fastapi.responses import Response

from create_map_poster import (
    generate_poster_bytes,
    get_available_themes,
    get_coordinates,
    load_theme,
)
from font_management import load_fonts
from lat_lon_parser import parse as parse_coords

app = FastAPI(
    title="Map to Poster API",
    description="Generate beautiful, minimalist map posters for any city.",
)

CONTENT_TYPES = {
    "png": "image/png",
    "svg": "image/svg+xml",
    "pdf": "application/pdf",
}


@app.get("/poster")
def get_poster(
    city: str = Query(..., description="City name"),
    country: str = Query(..., description="Country name"),
    theme: str = Query("terracotta", description="Theme name"),
    distance: int = Query(18000, description="Map radius in meters"),
    width: int = Query(3600, le=6000, description="Image width in pixels (max 6000)"),
    height: int = Query(4800, le=6000, description="Image height in pixels (max 6000)"),
    format: Literal["png", "svg", "pdf"] = Query("png", description="Output format"),
    latitude: Optional[str] = Query(None, description="Override latitude center point"),
    longitude: Optional[str] = Query(None, description="Override longitude center point"),
    display_city: Optional[str] = Query(None, description="Custom city display name (i18n)"),
    display_country: Optional[str] = Query(None, description="Custom country display name (i18n)"),
    font_family: Optional[str] = Query(None, description="Google Fonts family name"),
    country_label: Optional[str] = Query(None, description="Override country text on poster"),
    show_city: bool = Query(True, description="Show city name"),
    show_country: bool = Query(True, description="Show country name"),
    show_coords: bool = Query(True, description="Show coordinates"),
    show_attribution: bool = Query(True, description="Show attribution"),
    text_position: Literal["bottom", "top", "center"] = Query("bottom", description="Position of text labels"),
    font_size: Optional[float] = Query(None, description="Font size multiplier (e.g. 1.5 for 50% larger)"),
):
    available_themes = get_available_themes()
    if theme not in available_themes:
        return Response(
            status_code=400,
            content=f"Unknown theme '{theme}'. Available: {', '.join(available_themes)}",
            media_type="text/plain",
        )

    theme_data = load_theme(theme)

    custom_fonts = None
    if font_family:
        custom_fonts = load_fonts(font_family)

    try:
        if latitude is not None and longitude is not None:
            coords = [parse_coords(latitude), parse_coords(longitude)]
        else:
            coords = get_coordinates(city, country)

        image_bytes = generate_poster_bytes(
            city=city,
            country=country,
            point=coords,
            dist=distance,
            output_format=format,
            width=min(width, 6000),
            height=min(height, 6000),
            country_label=country_label,
            display_city=display_city,
            display_country=display_country,
            fonts=custom_fonts,
            theme=theme_data,
            show_city=show_city,
            show_country=show_country,
            show_coords=show_coords,
            show_attribution=show_attribution,
            text_position=text_position,
            font_size=font_size,
        )

        return Response(
            content=image_bytes,
            media_type=CONTENT_TYPES[format],
        )
    except ValueError as e:
        return Response(status_code=400, content=str(e), media_type="text/plain")
    except RuntimeError as e:
        return Response(status_code=502, content=str(e), media_type="text/plain")
    except Exception as e:
        return Response(status_code=500, content=str(e), media_type="text/plain")


@app.get("/themes")
def list_themes():
    return {"themes": get_available_themes()}
