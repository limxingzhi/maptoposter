# City Map Poster Generator

Generate beautiful, minimalist map posters for any city in the world.

<img src="posters/singapore_neon_cyberpunk_20260118_153328.png" width="250">
<img src="posters/dubai_midnight_blue_20260118_140807.png" width="250">

## Examples

| Country      | City           | Theme           | Poster |
|:------------:|:--------------:|:---------------:|:------:|
| USA          | San Francisco  | sunset          | <img src="posters/san_francisco_sunset_20260118_144726.png" width="250"> |
| Spain        | Barcelona      | warm_beige      | <img src="posters/barcelona_warm_beige_20260118_140048.png" width="250"> |
| Italy        | Venice         | blueprint       | <img src="posters/venice_blueprint_20260118_140505.png" width="250"> |
| Japan        | Tokyo          | japanese_ink    | <img src="posters/tokyo_japanese_ink_20260118_142446.png" width="250"> |
| India        | Mumbai         | contrast_zones  | <img src="posters/mumbai_contrast_zones_20260118_145843.png" width="250"> |
| Morocco      | Marrakech      | terracotta      | <img src="posters/marrakech_terracotta_20260118_143253.png" width="250"> |
| Singapore    | Singapore      | neon_cyberpunk  | <img src="posters/singapore_neon_cyberpunk_20260118_153328.png" width="250"> |
| Australia    | Melbourne      | forest          | <img src="posters/melbourne_forest_20260118_153446.png" width="250"> |
| UAE          | Dubai          | midnight_blue   | <img src="posters/dubai_midnight_blue_20260118_140807.png" width="250"> |
| USA          | Seattle        | emerald         | <img src="posters/seattle_emerald_20260124_162244.png" width="250"> |

## Installation

### With uv (Recommended)

Make sure [uv](https://docs.astral.sh/uv/) is installed. Running the script by prepending `uv run` automatically creates and manages a virtual environment.

```bash
# First run will automatically install dependencies
uv run ./create_map_poster.py --city "Paris" --country "France"

# Or sync dependencies explicitly first (using locked versions)
uv sync --locked
uv run ./create_map_poster.py --city "Paris" --country "France"
```

### With pip + venv

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Generate Poster

If you're using `uv`:

```bash
uv run ./create_map_poster.py --city <city> --country <country> [options]
```

Otherwise (pip + venv):

```bash
python create_map_poster.py --city <city> --country <country> [options]
```

### Required Options

| Option | Short | Description |
|--------|-------|-------------|
| `--city` | `-c` | City name (used for geocoding) |
| `--country` | `-C` | Country name (used for geocoding) |

### Optional Flags

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| **OPTIONAL:** `--latitude` | `-lat` | Override latitude center point (use with --longitude) | |
| **OPTIONAL:** `--longitude` | `-long` | Override longitude center point (use with --latitude) | |
| **OPTIONAL:** `--country-label` | | Override country text displayed on poster | |
| **OPTIONAL:** `--theme` | `-t` | Theme name | terracotta |
| **OPTIONAL:** `--distance` | `-d` | Map radius in meters | 18000 |
| **OPTIONAL:** `--list-themes` | | List all available themes | |
| **OPTIONAL:** `--all-themes` | | Generate posters for all available themes | |
| **OPTIONAL:** `--width` | `-W` | Image width in pixels | 3600 (max: 6000) |
| **OPTIONAL:** `--height` | `-H` | Image height in pixels | 4800 (max: 6000) |
| **OPTIONAL:** `--no-city` | | Hide city name on poster | shown |
| **OPTIONAL:** `--no-country` | | Hide country name on poster | shown |
| **OPTIONAL:** `--no-coords` | | Hide coordinates on poster | shown |
| **OPTIONAL:** `--no-attribution` | | Hide OSM attribution on poster | shown |

### Multilingual Support - i18n

Display city and country names in your language with custom fonts from google fonts:

| Option | Short | Description |
|--------|-------|-------------|
| `--display-city` | `-dc` | Custom display name for city (e.g., "東京") |
| `--display-country` | `-dC` | Custom display name for country (e.g., "日本") |
| `--font-family` | | Google Fonts family name (e.g., "Noto Sans JP") |

**Examples:**

```bash
# Japanese
python create_map_poster.py -c "Tokyo" -C "Japan" -dc "東京" -dC "日本" --font-family "Noto Sans JP"

# Korean
python create_map_poster.py -c "Seoul" -C "South Korea" -dc "서울" -dC "대한민국" --font-family "Noto Sans KR"

# Arabic
python create_map_poster.py -c "Dubai" -C "UAE" -dc "دبي" -dC "الإمارات" --font-family "Cairo"
```

**Note**: Fonts are automatically downloaded from Google Fonts and cached locally in `fonts/cache/`.

### Resolution Guide

Images are rendered at 300 DPI. Pass `--width` and `--height` in pixels:

| Target | `--width` `--height` |
|--------|----------------------|
| **Instagram Post** | `1080 1080` |
| **Mobile Wallpaper** | `1080 1920` |
| **HD Wallpaper** | `1920 1080` |
| **4K Wallpaper** | `3840 2160` |
| **A4 Print** | `2480 3508` |
| **Default (12×16 in print)** | `3600 4800` |

### Usage Examples

#### Basic Examples

```bash
# Simple usage with default theme
python create_map_poster.py -c "Paris" -C "France"

# With custom theme and distance
python create_map_poster.py -c "New York" -C "USA" -t noir -d 12000
```

#### Multilingual Examples (Non-Latin Scripts)

Display city names in their native scripts:

```bash
# Japanese
python create_map_poster.py -c "Tokyo" -C "Japan" -dc "東京" -dC "日本" --font-family "Noto Sans JP" -t japanese_ink

# Korean
python create_map_poster.py -c "Seoul" -C "South Korea" -dc "서울" -dC "대한민국" --font-family "Noto Sans KR" -t midnight_blue

# Thai
python create_map_poster.py -c "Bangkok" -C "Thailand" -dc "กรุงเทพมหานคร" -dC "ประเทศไทย" --font-family "Noto Sans Thai" -t sunset

# Arabic
python create_map_poster.py -c "Dubai" -C "UAE" -dc "دبي" -dC "الإمارات" --font-family "Cairo" -t terracotta

# Chinese (Simplified)
python create_map_poster.py -c "Beijing" -C "China" -dc "北京" -dC "中国" --font-family "Noto Sans SC"

# Khmer
python create_map_poster.py -c "Phnom Penh" -C "Cambodia" -dc "ភ្នំពេញ" -dC "កម្ពុជា" --font-family "Noto Sans Khmer"
```

#### Advanced Examples

```bash
# Iconic grid patterns
python create_map_poster.py -c "New York" -C "USA" -t noir -d 12000           # Manhattan grid
python create_map_poster.py -c "Barcelona" -C "Spain" -t warm_beige -d 8000   # Eixample district

# Waterfront & canals
python create_map_poster.py -c "Venice" -C "Italy" -t blueprint -d 4000       # Canal network
python create_map_poster.py -c "Amsterdam" -C "Netherlands" -t ocean -d 6000  # Concentric canals
python create_map_poster.py -c "Dubai" -C "UAE" -t midnight_blue -d 15000     # Palm & coastline

# Radial patterns
python create_map_poster.py -c "Paris" -C "France" -t pastel_dream -d 10000   # Haussmann boulevards
python create_map_poster.py -c "Moscow" -C "Russia" -t noir -d 12000          # Ring roads

# Organic old cities
python create_map_poster.py -c "Tokyo" -C "Japan" -t japanese_ink -d 15000    # Dense organic streets
python create_map_poster.py -c "Marrakech" -C "Morocco" -t terracotta -d 5000 # Medina maze
python create_map_poster.py -c "Rome" -C "Italy" -t warm_beige -d 8000        # Ancient layout

# Coastal cities
python create_map_poster.py -c "San Francisco" -C "USA" -t sunset -d 10000    # Peninsula grid
python create_map_poster.py -c "Sydney" -C "Australia" -t ocean -d 12000      # Harbor city
python create_map_poster.py -c "Mumbai" -C "India" -t contrast_zones -d 18000 # Coastal peninsula

# River cities
python create_map_poster.py -c "London" -C "UK" -t noir -d 15000              # Thames curves
python create_map_poster.py -c "Budapest" -C "Hungary" -t copper_patina -d 8000  # Danube split

# Override center coordinates
python create_map_poster.py --city "New York" --country "USA" -lat 40.776676 -long -73.971321 -t noir

# List available themes
python create_map_poster.py --list-themes

# Generate posters for every theme
python create_map_poster.py -c "Tokyo" -C "Japan" --all-themes
```

### Distance Guide

| Distance | Best for |
|----------|----------|
| 4000-6000m | Small/dense cities (Venice, Amsterdam center) |
| 8000-12000m | Medium cities, focused downtown (Paris, Barcelona) |
| 15000-20000m | Large metros, full city view (Tokyo, Mumbai) |

## Themes

17 themes available in `themes/` directory:

| Theme | Style |
|-------|-------|
| `gradient_roads` | Smooth gradient shading |
| `contrast_zones` | High contrast urban density |
| `noir` | Pure black background, white roads |
| `midnight_blue` | Navy background with gold roads |
| `blueprint` | Architectural blueprint aesthetic |
| `neon_cyberpunk` | Dark with electric pink/cyan |
| `warm_beige` | Vintage sepia tones |
| `pastel_dream` | Soft muted pastels |
| `japanese_ink` | Minimalist ink wash style |
| `emerald`      | Lush dark green aesthetic |
| `forest` | Deep greens and sage |
| `ocean` | Blues and teals for coastal cities |
| `terracotta` | Mediterranean warmth |
| `sunset` | Warm oranges and pinks |
| `autumn` | Seasonal burnt oranges and reds |
| `copper_patina` | Oxidized copper aesthetic |
| `monochrome_blue` | Single blue color family |

## Output

Posters are saved to `posters/` directory with format:

```text
{city}_{theme}_{YYYYMMDD_HHMMSS}.png
```

## Web Server

The application can also be run as an HTTP API server, returning poster images directly via `GET` requests.

### Starting the Server

With `uv`:

```bash
uv run uvicorn server:app --host 0.0.0.0 --port 8000
```

With `pip + venv`:

```bash
source .venv/bin/activate
uvicorn server:app --host 0.0.0.0 --port 8000
```

Add `--reload` for development (auto-restarts on code changes).

Interactive API documentation is available at `http://localhost:8000/docs` (Swagger UI).

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/poster` | Generate and return a map poster image |
| `GET` | `/themes` | List available theme names (JSON) |

### `GET /poster` Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `city` | City name (**required**) | |
| `country` | Country name (**required**) | |
| `theme` | Theme name | `terracotta` |
| `distance` | Map radius in meters | `18000` |
| `width` | Image width in pixels (max 6000) | `3600` |
| `height` | Image height in pixels (max 6000) | `4800` |
| `format` | Output format: `png`, `svg`, `pdf` | `png` |
| `latitude` | Override latitude center point | |
| `longitude` | Override longitude center point | |
| `display_city` | Custom city display name (i18n) | |
| `display_country` | Custom country display name (i18n) | |
| `font_family` | Google Fonts family name | |
| `country_label` | Override country text on poster | |
| `show_city` | Show city name | `true` |
| `show_country` | Show country name | `true` |
| `show_coords` | Show coordinates | `true` |
| `show_attribution` | Show attribution | `true` |

### Examples

```bash
# Basic poster
curl "http://localhost:8000/poster?city=Paris&country=France" -o paris.png

# Custom theme and zoom
curl "http://localhost:8000/poster?city=Tokyo&country=Japan&theme=japanese_ink&distance=15000" -o tokyo.png

# Multilingual with custom font
curl "http://localhost:8000/poster?city=Tokyo&country=Japan&display_city=%E6%9D%B1%E4%BA%AC&display_country=%E6%97%A5%E6%9C%AC&font_family=Noto+Sans+JP" -o tokyo_jp.png

# Override coordinates (Manhattan)
curl "http://localhost:8000/poster?city=New+York&country=USA&latitude=40.776676&longitude=-73.971321&theme=noir" -o manhattan.png

# List themes
curl "http://localhost:8000/themes"
```

### Docker

```bash
# Build
docker build -t maptoposter .

# Run (mount cache volume to persist OSM data between runs)
docker run --rm -p 8000:8000 -v $(pwd)/cache:/app/cache maptoposter

# Generate a poster
curl "http://localhost:8000/poster?city=London&country=UK&theme=noir" -o london.png
```

## Adding Custom Themes

Create a JSON file in `themes/` directory:

```json
{
  "name": "My Theme",
  "description": "Description of the theme",
  "bg": "#FFFFFF",
  "text": "#000000",
  "gradient_color": "#FFFFFF",
  "water": "#C0C0C0",
  "parks": "#F0F0F0",
  "road_motorway": "#0A0A0A",
  "road_primary": "#1A1A1A",
  "road_secondary": "#2A2A2A",
  "road_tertiary": "#3A3A3A",
  "road_residential": "#4A4A4A",
  "road_default": "#3A3A3A"
}
```

## Project Structure

```text
map_poster/
├── create_map_poster.py    # Main script (CLI)
├── server.py               # HTTP API server (FastAPI)
├── font_management.py      # Font loading and Google Fonts integration
├── Dockerfile              # Container definition
├── themes/                 # Theme JSON files
├── fonts/                  # Font files
│   ├── Roboto-*.ttf        # Default Roboto fonts
│   └── cache/              # Downloaded Google Fonts (auto-generated)
├── posters/                # Generated posters
├── cache/                  # Cached OSM data (auto-generated)
└── README.md
```


## Hacker's Guide

Quick reference for contributors who want to extend or modify the script.

### Contributors Guide

- Bug fixes are welcomed
- If you vibe code any fix please test it and see before and after version of poster
- Before embarking on a big feature please ask in Discussions/Issue if it will be merged

### Architecture Overview

```text
┌──────────────────────────────────────────────────────────────┐
│                      Entry Points                            │
│  ┌─────────────────┐         ┌────────────────────────────┐ │
│  │   CLI Parser    │         │    HTTP Server (FastAPI)    │ │
│  │   (argparse)    │         │    GET /poster, /themes     │ │
│  └────────┬────────┘         └─────────────┬──────────────┘ │
│           │                                │                │
└───────────┼────────────────────────────────┼────────────────┘
            │                                │
            ▼                                ▼
  ┌──────────────┐     ┌─────────────────┐
  │  Geocoding   │────▶│  Data Fetching  │
  │  (Nominatim) │     │    (OSMnx)      │
  └──────────────┘     └────────┬────────┘
                                │
               ┌──────────────┐ ▼
               │    Output    │ ┌─────────────────┐
               │  (matplotlib)│◀│   Rendering     │
               └──────────────┘ │  (matplotlib)   │
                                └─────────────────┘
```

### Key Functions

| Function | Purpose | Modify when... |
|----------|---------|----------------|
| `get_coordinates()` | City → lat/lon via Nominatim | Switching geocoding provider |
| `create_poster()` | Main rendering pipeline (file or buffer) | Adding new map layers |
| `generate_poster_bytes()` | Render poster to bytes (for HTTP server) | Changing server response format |
| `get_edge_colors_by_type()` | Road color by OSM highway tag | Changing road styling |
| `get_edge_widths_by_type()` | Road width by importance | Adjusting line weights |
| `create_gradient_fade()` | Top/bottom fade effect | Modifying gradient overlay |
| `load_theme()` | JSON theme → dict | Adding new theme properties |
| `is_latin_script()` | Detects script for typography | Supporting new scripts |
| `load_fonts()` | Load custom/default fonts | Changing font loading logic |

### Rendering Layers (z-order)

```text
z=11  Text labels (city, country, coords)
z=10  Gradient fades (top & bottom)
z=3   Roads (via ox.plot_graph)
z=2   Parks (green polygons)
z=1   Water (blue polygons)
z=0   Background color
```

### OSM Highway Types → Road Hierarchy

```python
# In get_edge_colors_by_type() and get_edge_widths_by_type()
motorway, motorway_link     → Thickest (1.2), darkest
trunk, primary              → Thick (1.0)
secondary                   → Medium (0.8)
tertiary                    → Thin (0.6)
residential, living_street  → Thinnest (0.4), lightest
```

### Typography & Script Detection

The script automatically detects text scripts to apply appropriate typography:

- **Latin scripts** (English, French, Spanish, etc.): Letter spacing applied for elegant "P  A  R  I  S" effect
- **Non-Latin scripts** (Japanese, Arabic, Thai, Korean, etc.): Natural spacing for "東京" (no gaps between characters)

Script detection uses Unicode ranges (U+0000-U+024F for Latin). If >80% of alphabetic characters are Latin, spacing is applied.

### Adding New Features

**New map layer (e.g., railways):**

```python
# In create_poster(), after parks fetch:
try:
    railways = ox.features_from_point(point, tags={'railway': 'rail'}, dist=dist)
except:
    railways = None

# Then plot before roads:
if railways is not None and not railways.empty:
    railways = railways.to_crs(g_proj.graph["crs"])
    railways.plot(ax=ax, color=THEME['railway'], linewidth=0.5, zorder=2.5)
```

**New theme property:**

1. Add to theme JSON: `"railway": "#FF0000"`
2. Use in code: `THEME['railway']`
3. Add fallback in `load_theme()` default dict

### Typography Positioning

All text uses `transform=ax.transAxes` (0-1 normalized coordinates):

```text
y=0.14  City name (spaced letters for Latin scripts)
y=0.125 Decorative line
y=0.10  Country name
y=0.07  Coordinates
y=0.02  Attribution (bottom-right)
```

### Useful OSMnx Patterns

```python
# Get all buildings
buildings = ox.features_from_point(point, tags={'building': True}, dist=dist)

# Get specific amenities
cafes = ox.features_from_point(point, tags={'amenity': 'cafe'}, dist=dist)

# Different network types
G = ox.graph_from_point(point, dist=dist, network_type='drive')  # roads only
G = ox.graph_from_point(point, dist=dist, network_type='bike')   # bike paths
G = ox.graph_from_point(point, dist=dist, network_type='walk')   # pedestrian
```

### Performance Tips

- Large `dist` values (>20km) = slow downloads + memory heavy
- Cache coordinates locally to avoid Nominatim rate limits
- Use `network_type='drive'` instead of `'all'` for faster renders
- Reduce `dpi` from 300 to 150 for quick previews
