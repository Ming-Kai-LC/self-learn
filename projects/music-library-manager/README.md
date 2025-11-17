# Music Library Manager

A comprehensive Jupyter notebook-based tool for managing, organizing, and maintaining your music collection.

## 📚 Available Modules

The project is organized into modular notebooks, each focusing on specific capabilities:

### ✅ Implemented Modules

- **[Module 00: Music Library Manager](notebooks/00_music_library_manager.ipynb)** - Core functionality
  - Library scanning and cataloging
  - Smart search and duplicate detection
  - Batch rename and move operations
  - Basic organization tools

- **[Module 01: Metadata Management](notebooks/01_metadata_management.ipynb)** - ID3 tags and metadata
  - Extract and display ID3 metadata (artist, album, title, genre, year)
  - Search by metadata fields, not just filenames
  - Identify files with missing/incomplete metadata
  - Parse filenames to extract metadata
  - Batch update and write metadata tags
  - Metadata quality analysis and reporting

- **[Module 02: Audio Analysis](notebooks/02_audio_analysis.ipynb)** - Quality detection and analysis
  - Extract audio properties (bitrate, sample rate, duration, channels)
  - Categorize files by quality tier (Poor/Low/Medium/High/Lossless)
  - Find low-quality files to upgrade
  - Enhanced duplicate detection with quality comparison
  - Smart recommendations on which duplicates to keep
  - Comprehensive audio quality reports

- **[Module 03: Album Art Management](notebooks/03_album_art_management.ipynb)** - Extract and manage album artwork
  - Extract embedded artwork from audio files
  - Analyze album art quality (resolution, file size, format)
  - Find files with missing or low-quality artwork
  - Embed album art into audio files
  - Batch extract unique artwork collection
  - Organize artwork by artist/album

- **[Module 04: Advanced Organization](notebooks/04_advanced_organization.ipynb)** - Metadata-based folder structures
  - Organize by Artist/Album hierarchy using metadata
  - Multiple folder templates (Artist/Album, Artist/Year-Album, Genre/Artist/Album, etc.)
  - Preview organization before applying changes
  - Safe file handling with automatic sanitization
  - Batch rename files with track numbers
  - Custom template support

- **[Module 06: Library Visualizations](notebooks/06_library_visualizations.ipynb)** - Charts and statistics
  - Format distribution pie charts
  - Quality tier bar charts and histograms
  - Genre and artist ranking visualizations
  - Bitrate distribution analysis
  - Library growth timeline
  - Interactive dashboards (with Plotly)
  - Comprehensive text and CSV reports

- **[Module 07: Playlist Management](notebooks/07_playlist_management.ipynb)** - Create and manage playlists
  - Create M3U and M3U8 playlists
  - Smart playlists by genre, artist, year, quality, album
  - Random playlist generation with constraints
  - Discovery playlists (exclude top artists)
  - Custom filter-based playlists
  - Playlist validation and integrity checking
  - Merge and manage multiple playlists

- **[Module 05: External API Integration](notebooks/05_external_api_integration.ipynb)** - Enrich metadata from online databases
  - Query MusicBrainz for authoritative metadata
  - Automatically download album art from Cover Art Archive
  - Batch enrich file metadata with correct information
  - Standardize artist/album names
  - API best practices (rate limiting, caching, error handling)
  - Fill in missing release dates and genres

- **[Module 08: Quality Validation and File Integrity](notebooks/08_quality_validation.ipynb)** - Health checks and maintenance
  - Detect corrupted or unreadable audio files
  - Validate metadata integrity and encoding
  - Find empty folders and orphaned files
  - Library health reports and statistics
  - Automated cleanup operations
  - Identify metadata quality issues

- **[Module 99: Complete Workflow](notebooks/99_complete_workflow.ipynb)** - End-to-end library management
  - Comprehensive workflow combining all modules
  - Step-by-step library assessment and enhancement
  - Quality control and organization workflow
  - Analysis, visualization, and playlist creation
  - Real-world examples and best practices
  - Complete library transformation in 90-120 minutes

## Features

### Core Functionality

- **Library Scanning**: Recursively scan your music directory and catalog all audio files
- **Smart Search**: Search for songs before downloading to avoid duplicates
- **Duplicate Detection**: Find duplicates using multiple methods:
  - Exact duplicates (by file hash)
  - Same file size
  - Similar filenames (fuzzy matching)
- **Auto-Organization**: Intelligently suggest and move files to appropriate folders based on name similarity
- **Batch Rename**: Clean up filenames with pattern matching
  - Remove common unwanted patterns ([Official Video], [HD], etc.)
  - Custom regex-based find and replace
  - Add prefixes to multiple files at once
- **Batch Move**: Organize files based on patterns and folder similarity

### Supported Audio Formats

- MP3 (.mp3)
- FLAC (.flac)
- WAV (.wav)
- M4A (.m4a)
- AAC (.aac)
- OGG (.ogg)
- WMA (.wma)
- OPUS (.opus)

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Jupyter**:
   ```bash
   jupyter notebook notebooks/00_music_library_manager.ipynb
   ```

3. **Configure your music path**:
   - Edit the `MUSIC_LIBRARY_PATH` variable in the notebook
   - Default: `../../music` (points to `/home/user/self-learn/music`)

4. **Run the cells** to start managing your music!

## Usage Examples

### Check Before Downloading

```python
# Search for a song to see if you already have it
search_query = "beatles hey jude"
results = search_songs(search_query, all_music_files)

if len(results) > 0:
    print("You already have this song!")
    display(results)
```

### Find Duplicates

```python
# Quick check: Find files with identical sizes
same_size = find_same_size_duplicates(all_music_files)

# More thorough: Find exact duplicates by file content
exact_dupes = find_exact_duplicates(all_music_files)

# Fuzzy matching: Find similar filenames
similar = find_similar_names(all_music_files, threshold=0.85)
```

### Clean Filenames

```python
# Remove unwanted patterns like [Official Video], (HD), etc.
cleanup_actions = batch_clean_names(MUSIC_LIBRARY_PATH, dry_run=True)
display(pd.DataFrame(cleanup_actions))

# Apply changes
cleanup_actions = batch_clean_names(MUSIC_LIBRARY_PATH, dry_run=False)
```

### Auto-Organize Files

```python
# Move files from root to folders with similar names
organize_actions = batch_move_similar_to_folders(
    MUSIC_LIBRARY_PATH,
    threshold=0.7,
    dry_run=True  # Preview first
)

# Apply changes
organize_actions = batch_move_similar_to_folders(
    MUSIC_LIBRARY_PATH,
    threshold=0.7,
    dry_run=False
)
```

### Batch Rename

```python
# Custom pattern replacement
pattern = r"old_text"
replacement = "new_text"
actions = batch_rename(folder_path, pattern, replacement, dry_run=True)

# Add prefix to all files
actions = batch_add_prefix(folder_path, "Artist - ", dry_run=True)
```

## Complete Workflow

Process new downloads automatically:

```python
downloads_path = Path("/path/to/downloads")
manage_new_downloads_workflow(downloads_path, MUSIC_LIBRARY_PATH)
```

This workflow will:
1. Scan downloads folder
2. Check for duplicates
3. Clean filenames
4. Organize into appropriate folders

## Safety Features

- **Dry-run mode**: All operations support preview mode (`dry_run=True`)
- **Duplicate prevention**: Always checks if target file exists before moving/renaming
- **Confidence scores**: Shows how confident the system is about suggestions
- **Relative paths**: Uses relative paths for portability

## Configuration

### Adjust Similarity Thresholds

Control how aggressive the auto-organization is:

```python
# Conservative (only very similar names)
threshold = 0.9

# Balanced (default)
threshold = 0.7

# Aggressive (move more files, may have false positives)
threshold = 0.5
```

### Custom Audio Extensions

Add support for additional formats:

```python
AUDIO_EXTENSIONS.add('.custom_format')
```

## Project Structure

```
music-library-manager/
├── notebooks/
│   └── 00_music_library_manager.ipynb  # Main notebook
├── requirements.txt                     # Python dependencies
└── README.md                           # This file
```

## Best Practices

1. **Always preview first**: Use `dry_run=True` to see what will happen
2. **Backup your library**: Keep backups before bulk operations
3. **Start small**: Test on a subset of files before processing everything
4. **Adjust thresholds**: Fine-tune similarity matching for your needs
5. **Regular maintenance**: Run duplicate detection periodically

## Tips and Tricks

### Regex Pattern Examples

```python
# Remove text in parentheses
pattern = r"\(.*?\)"
replacement = ""

# Replace multiple spaces with single space
pattern = r"\s+"
replacement = " "

# Remove leading numbers
pattern = r"^\d+\s*-\s*"
replacement = ""
```

### Working with Specific Folders

```python
# Process only a specific subfolder
specific_folder = MUSIC_LIBRARY_PATH / "Artist Name"
actions = batch_clean_names(specific_folder)
```

### Statistics and Analysis

```python
# Get detailed library statistics
stats = get_library_stats(all_music_files)
print(f"Total: {stats['total_files']} files, {stats['total_size_gb']} GB")
```

## Troubleshooting

**Issue**: Files not being found
- Check that `MUSIC_LIBRARY_PATH` is correct
- Verify the file extensions are in `AUDIO_EXTENSIONS`

**Issue**: Too many/few auto-organization suggestions
- Adjust the `threshold` parameter (0.5-0.9)
- Lower = more matches, Higher = only very similar matches

**Issue**: Unwanted patterns not being cleaned
- Add custom patterns to `batch_clean_names` function
- Use regex tester to validate your patterns

## Future Enhancements

Potential additions to this notebook:

- ID3 tag metadata extraction and editing
- Album art management
- Playlist creation and management
- Audio quality analysis
- Integration with music databases (MusicBrainz, Last.fm)
- Automatic folder creation based on artist/album
- Visualizations of music collection stats

## Dependencies

- Python 3.7+
- pandas: Data manipulation and display
- IPython: Rich display in Jupyter

All dependencies are listed in `requirements.txt`.

## License

This project is part of the self-learning portfolio.

## Contributing

This is a personal learning project. Feel free to fork and customize for your needs!
