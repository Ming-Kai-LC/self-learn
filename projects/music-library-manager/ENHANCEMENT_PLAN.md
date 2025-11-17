# Music Library Manager - Enhancement Plan

## Current Features ✓

### Core Functionality
- ✅ Recursive library scanning with file metadata
- ✅ Smart search by filename
- ✅ Duplicate detection (hash, size, name similarity)
- ✅ Auto-organization with confidence scoring
- ✅ Batch rename operations (clean, pattern replace, prefix)
- ✅ Batch move operations
- ✅ Complete workflow automation
- ✅ Dry-run mode for all operations
- ✅ Support for 8 audio formats (MP3, FLAC, WAV, M4A, AAC, OGG, WMA, OPUS)

---

## Enhancement Roadmap

### 🎯 Phase 1: Metadata Extraction and Management
**Priority:** HIGH | **Difficulty:** ⭐⭐ | **Estimated Time:** 2-3 hours

#### Features to Add:

1. **ID3 Tag Reading**
   - Extract metadata: artist, album, title, year, genre, track number
   - Display metadata in library scan results
   - Search by metadata (not just filename)
   - Show files with missing/incomplete metadata

2. **ID3 Tag Writing/Editing**
   - Batch update metadata from filenames (parse "Artist - Title.mp3")
   - Standardize metadata across library
   - Auto-fill missing metadata from filename patterns
   - Fix common metadata issues (encoding, case)

3. **Smart Metadata Analysis**
   - Identify files with missing critical tags
   - Detect inconsistent artist/album naming
   - Suggest metadata corrections
   - Report metadata quality score per file

#### Implementation Details:
```python
# New library: mutagen
import mutagen
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3

# New functions to add:
def extract_metadata(file_path) -> Dict
def batch_update_metadata(files, metadata_dict) -> List[Dict]
def parse_filename_to_metadata(filename) -> Dict
def find_files_with_missing_metadata(music_files) -> pd.DataFrame
def get_metadata_quality_score(file_path) -> float
```

#### Use Cases:
- "Show me all songs with missing artist tags"
- "Auto-tag files using their filenames"
- "Find all songs from 'Beatles' (even if filename doesn't match)"

---

### 🎯 Phase 2: Audio Analysis and Quality Detection
**Priority:** HIGH | **Difficulty:** ⭐⭐ | **Estimated Time:** 2-3 hours

#### Features to Add:

1. **Audio Properties Extraction**
   - Bitrate (CBR/VBR detection)
   - Sample rate (44.1kHz, 48kHz, etc.)
   - Duration (length in minutes:seconds)
   - Channels (mono/stereo)
   - Codec information

2. **Quality Analysis**
   - Categorize by quality tier (Low: <128kbps, Medium: 128-256kbps, High: >256kbps, Lossless)
   - Find low-quality files that could be upgraded
   - Compare quality of duplicates
   - Report average library quality

3. **Advanced Duplicate Handling**
   - Compare audio properties of duplicates
   - Suggest which duplicate to keep (prefer higher quality)
   - Auto-remove lower quality duplicates (with confirmation)
   - Smart duplicate resolution workflow

#### Implementation Details:
```python
# Use mutagen for audio properties
def get_audio_properties(file_path) -> Dict
def categorize_audio_quality(bitrate, format) -> str
def compare_duplicate_quality(file1, file2) -> Dict
def suggest_duplicate_to_keep(duplicates) -> List[Dict]
def find_low_quality_files(threshold_kbps=128) -> pd.DataFrame

# Enhanced duplicate detection
def find_duplicates_with_quality_comparison(music_files) -> Dict
```

#### Use Cases:
- "Find all low-quality MP3s that I should re-download"
- "Show me duplicate files and which one to keep"
- "What's the average bitrate of my library?"
- "Find all FLAC files (lossless)"

---

### 🎯 Phase 3: Album Art Management
**Priority:** MEDIUM | **Difficulty:** ⭐⭐⭐ | **Estimated Time:** 3-4 hours

#### Features to Add:

1. **Album Art Extraction**
   - Extract embedded album art from files
   - Save album art as separate images
   - Display album art in notebook
   - Identify files missing album art

2. **Album Art Management**
   - Add/embed album art to files
   - Remove album art (reduce file size)
   - Standardize album art size/format
   - Batch operations for album art

3. **Album Art Download (Optional)**
   - Search for album art online (Last.fm, MusicBrainz)
   - Download and embed automatically
   - Manual selection from multiple options

#### Implementation Details:
```python
# New libraries: Pillow for image handling
from PIL import Image
import mutagen
from mutagen.id3 import APIC

# New functions:
def extract_album_art(file_path, output_path=None) -> bool
def embed_album_art(file_path, image_path) -> bool
def remove_album_art(file_path) -> bool
def find_files_without_album_art(music_files) -> pd.DataFrame
def resize_album_art(image_path, max_size=600) -> bool
def batch_embed_album_art(folder_path, image_path) -> List[Dict]
```

#### Use Cases:
- "Show me all songs missing album art"
- "Extract all album art to a folder"
- "Add this album cover to all songs in the 'Beatles' folder"
- "Remove album art to reduce file sizes"

---

### 🎯 Phase 4: Advanced Folder Organization
**Priority:** HIGH | **Difficulty:** ⭐⭐ | **Estimated Time:** 2-3 hours

#### Features to Add:

1. **Structured Folder Organization**
   - Create Artist/Album/Track hierarchy
   - Move files to structured folders automatically
   - Support multiple naming conventions
   - Template-based folder structure

2. **Smart Folder Creation**
   - Auto-create folders from metadata
   - Group by: Artist, Album, Year, Genre
   - Support custom folder templates
   - Preview folder structure before applying

3. **Folder Naming Conventions**
   - Standardize folder names
   - Handle special characters safely
   - Support various conventions (Artist - Album, Artist/Year - Album, etc.)

#### Implementation Details:
```python
# Folder structure templates
FOLDER_TEMPLATES = {
    'artist_album': '{artist}/{album}',
    'artist_year_album': '{artist}/{year} - {album}',
    'genre_artist_album': '{genre}/{artist}/{album}',
    'year_artist_album': '{year}/{artist} - {album}'
}

# New functions:
def create_folder_structure(template, music_files, dry_run=True) -> List[Dict]
def organize_by_metadata(library_path, template='artist_album', dry_run=True) -> List[Dict]
def preview_folder_structure(music_files, template) -> str
def standardize_folder_names(library_path) -> List[Dict]
def validate_folder_structure(library_path, template) -> Dict
```

#### Use Cases:
- "Organize my entire library as Artist/Album/Songs"
- "Create folders by genre, then artist"
- "Reorganize using metadata instead of filenames"
- "Preview how my library would look with Artist/Year - Album structure"

---

### 🎯 Phase 5: External API Integrations
**Priority:** MEDIUM | **Difficulty:** ⭐⭐⭐ | **Estimated Time:** 4-5 hours

#### Features to Add:

1. **MusicBrainz Integration**
   - Search for song/album information
   - Auto-tag files with accurate metadata
   - Verify existing metadata against database
   - Fetch missing information

2. **Last.fm Integration (Optional)**
   - Fetch song statistics (play counts, similar artists)
   - Get tag suggestions (genre, mood)
   - Scrobbling support

3. **Lyrics Fetching (Optional)**
   - Download lyrics for songs
   - Embed lyrics in metadata
   - Display lyrics in notebook

#### Implementation Details:
```python
# New libraries: musicbrainzngs, pylast
import musicbrainzngs
import requests

# New functions:
def search_musicbrainz(artist, album, title) -> Dict
def fetch_metadata_from_musicbrainz(music_files) -> List[Dict]
def verify_metadata_accuracy(file_path) -> Dict
def fetch_lyrics(artist, title) -> str
def batch_auto_tag_from_api(music_files, confidence_threshold=0.8) -> List[Dict]
```

#### Use Cases:
- "Auto-tag my entire library using MusicBrainz"
- "Verify if my metadata is accurate"
- "Download lyrics for all songs"
- "Find official release information for this album"

**Note:** Requires API keys and rate limiting considerations.

---

### 🎯 Phase 6: Visualizations and Statistics
**Priority:** MEDIUM | **Difficulty:** ⭐⭐ | **Estimated Time:** 2-3 hours

#### Features to Add:

1. **Library Statistics Dashboard**
   - Interactive charts and graphs
   - Distribution by format, quality, year, genre
   - Storage usage breakdown
   - Growth over time (if tracked)

2. **Visual Analytics**
   - Genre distribution pie chart
   - Bitrate quality distribution
   - Artist/album bar charts (top 10)
   - File size heatmap
   - Timeline of music collection

3. **Reporting**
   - Generate HTML reports
   - Export statistics to CSV
   - Library health score
   - Recommendations based on analysis

#### Implementation Details:
```python
# New libraries: matplotlib, seaborn, plotly
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# New functions:
def plot_format_distribution(music_files)
def plot_quality_distribution(music_files)
def plot_genre_breakdown(music_files)
def plot_artist_top_n(music_files, n=10)
def plot_library_timeline(music_files)
def generate_library_health_report(music_files) -> Dict
def create_interactive_dashboard(music_files)
def export_statistics_report(music_files, output_path)
```

#### Use Cases:
- "Show me a chart of my music by genre"
- "What's the quality distribution of my library?"
- "Which artists do I have the most songs from?"
- "Generate a library health report"

---

### 🎯 Phase 7: Playlist Management
**Priority:** MEDIUM | **Difficulty:** ⭐⭐ | **Estimated Time:** 2-3 hours

#### Features to Add:

1. **Playlist Creation**
   - Create M3U/M3U8 playlists
   - Add songs by criteria (genre, artist, year)
   - Manual playlist building
   - Import/export playlists

2. **Smart Playlists**
   - Auto-generate based on rules
   - Dynamic playlists (update automatically)
   - Criteria: genre, year range, bitrate, duration
   - Random selection with constraints

3. **Playlist Management**
   - List all playlists
   - Edit existing playlists
   - Merge/split playlists
   - Validate playlist files exist

#### Implementation Details:
```python
# M3U playlist format support
def create_playlist(name, file_list, format='m3u8') -> str
def create_smart_playlist(criteria, name) -> str
def import_playlist(playlist_path) -> List[str]
def validate_playlist(playlist_path) -> Dict
def merge_playlists(playlist_paths, output_name) -> str

# Smart playlist criteria
def select_by_genre(genre, limit=None) -> List[Dict]
def select_by_year_range(start_year, end_year) -> List[Dict]
def select_random(count, criteria=None) -> List[Dict]
def select_by_quality(min_bitrate) -> List[Dict]
```

#### Use Cases:
- "Create a playlist of all Rock songs"
- "Make a 'Best of 80s' playlist"
- "Generate a random playlist of 50 high-quality songs"
- "Create a playlist of all Beatles songs"

---

### 🎯 Phase 8: Quality Checks and Validation
**Priority:** HIGH | **Difficulty:** ⭐⭐⭐ | **Estimated Time:** 3-4 hours

#### Features to Add:

1. **File Integrity Validation**
   - Detect corrupted audio files
   - Verify file headers
   - Test file playability
   - Identify incomplete downloads

2. **Metadata Validation**
   - Find files with missing critical tags
   - Detect encoding issues
   - Identify malformed metadata
   - Suggest fixes

3. **Library Health Checks**
   - Orphaned files (not in folders)
   - Empty folders
   - Duplicate folders
   - Naming convention violations
   - File permission issues

4. **Automated Maintenance**
   - Schedule periodic scans
   - Auto-fix common issues
   - Generate maintenance reports
   - Suggest optimization actions

#### Implementation Details:
```python
# New libraries: audioread for validation
import audioread

# New functions:
def validate_file_integrity(file_path) -> Dict
def test_audio_playability(file_path) -> bool
def find_corrupted_files(music_files) -> List[Dict]
def validate_metadata_encoding(file_path) -> bool
def find_orphaned_files(library_path) -> List[str]
def find_empty_folders(library_path) -> List[str]
def run_library_health_check(library_path) -> Dict
def generate_maintenance_report(library_path) -> str
def auto_fix_common_issues(library_path, dry_run=True) -> List[Dict]
```

#### Use Cases:
- "Find all corrupted or unplayable files"
- "Check for metadata encoding issues"
- "Show me all empty folders"
- "Run a complete library health check"
- "Fix common issues automatically"

---

## Implementation Priority

### 🔥 Phase 1 (Start Here)
**High Impact, Quick Wins:**
1. ✅ Phase 1: Metadata Extraction (2-3 hours) - FOUNDATION
2. ✅ Phase 2: Audio Quality Analysis (2-3 hours) - HIGH VALUE
3. ✅ Phase 4: Advanced Folder Organization (2-3 hours) - IMMEDIATE BENEFIT

**Total Time:** ~7-9 hours

### 🎨 Phase 2 (Enhance Experience)
**Medium Priority, Valuable Features:**
4. ✅ Phase 6: Visualizations (2-3 hours) - BETTER INSIGHTS
5. ✅ Phase 7: Playlist Management (2-3 hours) - PRACTICAL UTILITY
6. ✅ Phase 8: Quality Checks (3-4 hours) - MAINTENANCE

**Total Time:** ~7-10 hours

### 🚀 Phase 3 (Advanced Features) - ✅ **COMPLETE**
**Optional, Nice-to-Have:**
7. ✅ Phase 3: Album Art Management (3-4 hours) - VISUAL APPEAL - **Module 03**
8. ✅ Phase 5: External API Integration (4-5 hours) - ADVANCED - **Module 05**
9. ✅ Phase 8: Quality Validation (3-4 hours) - MAINTENANCE - **Module 08**

**Total Time:** ~10-12 hours
**Status:** ✅ All modules implemented and tested

---

## Technical Dependencies

### New Libraries Required:

```txt
# Phase 1 & 2 (Implemented) ✅
mutagen>=1.45.0         # Audio metadata handling

# Phase 3 (Implemented) ✅
Pillow>=8.0.0           # Image processing for album art
musicbrainzngs>=0.7.1   # MusicBrainz API
requests>=2.25.0        # HTTP requests for API calls

# Phase 2 Visualizations (Implemented) ✅
matplotlib>=3.3.0       # Static visualizations
seaborn>=0.11.0         # Enhanced statistical plots
numpy>=1.20.0           # Numerical operations

# Phase 2 Optional
plotly>=5.0.0           # Interactive visualizations (install separately)

# Future Enhancements
audioread>=2.1.9        # Audio file validation (future)
pylast>=5.0.0           # Last.fm API (future)
requests>=2.26.0        # HTTP requests for lyrics
```

### Recommended Structure:

```
music-library-manager/
├── notebooks/
│   ├── 00_music_library_manager.ipynb          # Current (basic features)
│   ├── 01_metadata_management.ipynb            # Phase 1
│   ├── 02_audio_analysis.ipynb                 # Phase 2
│   ├── 03_album_art_manager.ipynb              # Phase 3
│   ├── 04_advanced_organization.ipynb          # Phase 4
│   ├── 05_api_integrations.ipynb               # Phase 5
│   ├── 06_library_visualizations.ipynb         # Phase 6
│   ├── 07_playlist_manager.ipynb               # Phase 7
│   ├── 08_quality_validation.ipynb             # Phase 8
│   └── 99_complete_music_manager.ipynb         # All-in-one (final)
├── src/
│   ├── __init__.py
│   ├── scanner.py        # Library scanning
│   ├── metadata.py       # Metadata operations
│   ├── audio.py          # Audio analysis
│   ├── organizer.py      # Organization logic
│   ├── duplicates.py     # Duplicate detection
│   ├── visualization.py  # Charts and graphs
│   ├── playlists.py      # Playlist management
│   └── validation.py     # Quality checks
├── data/
│   └── playlists/        # Generated playlists
├── tests/
│   └── test_*.py         # Unit tests
├── requirements.txt
└── README.md
```

---

## Breaking Changes

### Current Code Modifications:

1. **Extend `scan_music_library()` to include metadata:**
```python
# Before
music_files.append({
    'filename': file,
    'path': str(file_path),
    'folder': str(file_path.parent.relative_to(library_path)),
    'size_mb': stat_info.st_size / (1024 * 1024),
    'modified': datetime.fromtimestamp(stat_info.st_mtime),
    'extension': file_path.suffix.lower()
})

# After (Phase 1)
metadata = extract_metadata(file_path)
audio_props = get_audio_properties(file_path)
music_files.append({
    'filename': file,
    'path': str(file_path),
    'folder': str(file_path.parent.relative_to(library_path)),
    'size_mb': stat_info.st_size / (1024 * 1024),
    'modified': datetime.fromtimestamp(stat_info.st_mtime),
    'extension': file_path.suffix.lower(),
    # NEW FIELDS
    'artist': metadata.get('artist'),
    'album': metadata.get('album'),
    'title': metadata.get('title'),
    'year': metadata.get('date'),
    'genre': metadata.get('genre'),
    'track_number': metadata.get('tracknumber'),
    'bitrate': audio_props.get('bitrate'),
    'sample_rate': audio_props.get('sample_rate'),
    'duration': audio_props.get('length'),
    'quality_tier': categorize_audio_quality(audio_props.get('bitrate'))
})
```

2. **Enhanced search to include metadata:**
```python
def search_songs(query, music_files, search_in=['filename', 'artist', 'album', 'title']):
    # Search across multiple fields
    ...
```

---

## Expected Outcomes

After all phases are complete, users will be able to:

### Metadata Management
- ✅ View complete metadata for all songs
- ✅ Auto-tag files from filenames
- ✅ Find and fix metadata issues
- ✅ Search by artist, album, title, genre

### Organization
- ✅ Organize library in Artist/Album structure
- ✅ Auto-organize new downloads
- ✅ Support multiple folder templates
- ✅ Batch operations on entire library

### Quality Control
- ✅ Identify low-quality files
- ✅ Find and resolve duplicates intelligently
- ✅ Detect corrupted files
- ✅ Run health checks

### Discovery & Analysis
- ✅ Visualize library statistics
- ✅ Generate reports
- ✅ Create smart playlists
- ✅ Track library growth

### Advanced Features
- ✅ Manage album art
- ✅ Fetch metadata from online databases
- ✅ Download lyrics
- ✅ Export library catalog

---

## Next Steps

1. **Review this plan** with the user
2. **Prioritize phases** based on user needs
3. **Start with Phase 1** (Metadata Extraction)
4. **Implement incrementally** with testing between phases
5. **Update documentation** as features are added
6. **Consider modular approach** (separate notebooks or all-in-one)

---

## Questions for User

Before proceeding, please confirm:

1. **Priority:** Which phases are most important to you?
2. **Approach:** Separate notebooks for each phase, or enhance the current notebook?
3. **Testing:** Do you have a sample music library to test with?
4. **API Keys:** For Phase 5, do you want to set up MusicBrainz/Last.fm accounts?
5. **Scope:** Any specific features not listed that you need?

---

## Implementation Status

### ✅ **COMPLETED PHASES (100% of planned features)**

**Phase 1:** Metadata Management - **Module 01** ✅
**Phase 2:** Audio Analysis - **Module 02** ✅
**Phase 3:** Album Art Management - **Module 03** ✅
**Phase 4:** Advanced Organization - **Module 04** ✅
**Phase 5:** External API Integration - **Module 05** ✅
**Phase 6:** Visualizations - **Module 06** ✅
**Phase 7:** Playlist Management - **Module 07** ✅
**Phase 8:** Quality Validation - **Module 08** ✅

**Total Modules:** 9 (including base Module 00)
**Total Development Time:** ~25-30 hours
**All features implemented and documented!** 🎉

---

**Created:** 2025-11-17
**Last Updated:** 2025-11-17
**Status:** ✅ **COMPLETE** - All 8 phases implemented
**Version:** 1.5
