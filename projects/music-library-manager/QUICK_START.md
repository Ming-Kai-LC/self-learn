# Music Library Manager - Quick Start Guide

Welcome to your comprehensive music library management system! This guide will help you get started quickly.

## 🚀 Installation (5 minutes)

### 1. Install Dependencies

```bash
cd /home/user/self-learn/projects/music-library-manager
pip install -r requirements.txt
```

**Required packages:**
- `pandas` - Data manipulation
- `mutagen` - Audio metadata handling
- `matplotlib` - Charts and graphs
- `seaborn` - Enhanced visualizations
- `numpy` - Numerical operations

**Optional (for interactive dashboards):**
```bash
pip install plotly
```

### 2. Verify Installation

```bash
python -c "import mutagen, pandas, matplotlib; print('✓ All required packages installed')"
```

---

## 📁 Add Your Music

Place your music files in the music folder:

```bash
# Music folder location
/home/user/self-learn/music/

# Supported formats:
# MP3, FLAC, WAV, M4A, AAC, OGG, WMA, OPUS
```

You can organize music however you want - the tools will help you reorganize it!

---

## 🎯 Your First Session (10 minutes)

### Option 1: Quick Overview

Launch Jupyter and run **Module 00** for basic operations:

```bash
jupyter notebook notebooks/00_music_library_manager.ipynb
```

**What you'll do:**
1. Scan your library (count files)
2. Search for songs
3. Find duplicates
4. View basic statistics

### Option 2: Start with Metadata

Launch **Module 01** to understand your library's metadata:

```bash
jupyter notebook notebooks/01_metadata_management.ipynb
```

**What you'll do:**
1. See what metadata you have (artist, album, title)
2. Find files with missing metadata
3. Auto-tag files from filenames
4. Get a metadata quality report

---

## 🎨 Common Workflows

### Workflow 1: Analyze Your Library (15 minutes)

**Goal:** Understand what music you have and its quality

1. **Module 01** - Check metadata completeness
2. **Module 02** - Analyze audio quality
3. **Module 06** - Create visualizations

```python
# In Module 01
files = scan_library_with_metadata(MUSIC_LIBRARY_PATH)
report = get_metadata_quality_report(files)
print(f"Average completeness: {report['average_completeness']}%")

# In Module 02
files = scan_library_with_audio_analysis(MUSIC_LIBRARY_PATH)
stats = get_quality_statistics(files)
# See quality distribution

# In Module 06
files = scan_library_full(MUSIC_LIBRARY_PATH)
plot_quality_distribution(files)
plot_top_artists(files)
```

**Expected outcome:** You'll know:
- How complete your metadata is
- What quality your files are
- What genres/artists dominate your library
- Which files need upgrading

---

### Workflow 2: Clean Up and Organize (30 minutes)

**Goal:** Organize your library with Artist/Album structure

1. **Module 01** - Fix missing metadata
2. **Module 02** - Find and resolve duplicates
3. **Module 04** - Reorganize with Artist/Album folders

```python
# Step 1: Auto-tag files missing metadata
files = scan_library_with_metadata(MUSIC_LIBRARY_PATH)
actions = batch_update_from_filename(files, dry_run=True)  # Preview
actions = batch_update_from_filename(files, dry_run=False) # Execute

# Step 2: Find duplicates
files = scan_library_with_audio_analysis(MUSIC_LIBRARY_PATH)
duplicates = find_duplicates_with_quality(files, method='size')
# Review and remove lower quality duplicates manually

# Step 3: Reorganize by Artist/Album
files = scan_for_organization(MUSIC_LIBRARY_PATH)
plan = plan_organization(files, FOLDER_TEMPLATES['artist_album'])
preview_folder_structure(plan)  # Review structure
execute_organization(MUSIC_LIBRARY_PATH, plan, dry_run=True)   # Preview
execute_organization(MUSIC_LIBRARY_PATH, plan, dry_run=False)  # Execute
cleanup_empty_folders(MUSIC_LIBRARY_PATH, dry_run=False)
```

**Expected outcome:**
- All files have proper metadata
- Duplicates identified and resolved
- Library organized as: `Artist/Album/Songs`
- Empty folders cleaned up

---

### Workflow 3: Create Playlists (10 minutes)

**Goal:** Make playlists for different occasions

```python
# In Module 07
files = scan_library_for_playlists(MUSIC_LIBRARY_PATH)

# Create genre playlists
create_smart_playlist_by_genre(files, "rock", "rock_collection")
create_smart_playlist_by_genre(files, "jazz", "jazz_relaxation")

# Create decade playlists
create_smart_playlist_by_year(files, 1980, 1989, "80s_classics")
create_smart_playlist_by_year(files, 2000, 2009, "2000s_hits")

# High-quality playlist
create_smart_playlist_by_quality(files, ['lossless', 'high'], "audiophile_collection")

# Random discovery
create_random_playlist(files, count=50, playlist_name="random_50")
create_discovery_playlist(files, count=30, playlist_name="hidden_gems")

# View created playlists
playlists = list_playlists()
```

**Expected outcome:**
- Multiple playlists in `music/playlists/` folder
- Can copy to phone, car, or use with media players
- Discover forgotten music

---

## 🎓 Learning Path by Module

### **Beginner Track** (1-2 hours)

1. **Module 00** (15 min) - Learn the basics
   - Scan library
   - Search for songs
   - Basic statistics

2. **Module 01** (30 min) - Understand metadata
   - View metadata
   - Search by artist/album
   - Find missing metadata

3. **Module 07** (30 min) - Create playlists
   - Smart playlists by genre
   - Random playlists
   - Validate playlists

### **Intermediate Track** (2-4 hours)

4. **Module 02** (45 min) - Audio quality
   - Quality tier analysis
   - Find low-quality files
   - Smart duplicate detection

5. **Module 06** (30 min) - Visualizations
   - Create charts
   - View library statistics
   - Export reports

6. **Module 04** (1 hour) - Advanced organization
   - Metadata-based organization
   - Folder templates
   - Batch operations

### **Advanced Track** (Ongoing)

- Create custom smart playlists with complex filters
- Automate library maintenance workflows
- Develop custom organization templates
- Build interactive dashboards
- Integrate with external tools

---

## 📊 Module Overview & Use Cases

| Module | Best For | Time | Difficulty |
|--------|----------|------|------------|
| **00** | First-time users, basic operations | 15 min | ⭐ |
| **01** | Metadata cleanup, tagging | 30 min | ⭐⭐ |
| **02** | Quality control, duplicate removal | 45 min | ⭐⭐ |
| **03** | Album art extraction and management | 45 min | ⭐⭐ |
| **04** | Library reorganization | 1 hour | ⭐⭐⭐ |
| **05** | Metadata enrichment from APIs | 1 hour | ⭐⭐⭐ |
| **06** | Visual analysis, reports | 30 min | ⭐⭐ |
| **07** | Playlist creation, discovery | 30 min | ⭐⭐ |
| **08** | Quality validation, health checks | 45 min | ⭐⭐ |

---

## 🎯 Quick Reference: Most Useful Functions

### Scanning
```python
# Basic scan
all_files = scan_music_library(MUSIC_LIBRARY_PATH)

# With metadata
all_files = scan_library_with_metadata(MUSIC_LIBRARY_PATH)

# With audio analysis
all_files = scan_library_with_audio_analysis(MUSIC_LIBRARY_PATH)

# For playlists
all_files = scan_library_for_playlists(MUSIC_LIBRARY_PATH)
```

### Searching
```python
# Search by filename
results = search_songs("query", all_files)

# Search by metadata
results = search_by_artist(all_files, "beatles")
results = search_by_album(all_files, "abbey road")
results = search_by_genre(all_files, "rock")
```

### Metadata Operations
```python
# Find missing metadata
missing = find_files_with_missing_metadata(all_files)

# Auto-tag from filenames
batch_update_from_filename(all_files, dry_run=False)

# Quality report
report = get_metadata_quality_report(all_files)
```

### Quality Analysis
```python
# Get statistics
stats = get_quality_statistics(all_files)

# Find low quality
low_quality = find_low_quality_files(all_files, threshold='medium')

# Find duplicates with quality info
duplicates = find_duplicates_with_quality(all_files)
```

### Organization
```python
# Plan organization
plan = plan_organization(all_files, FOLDER_TEMPLATES['artist_album'])

# Preview
preview_folder_structure(plan)

# Execute
execute_organization(MUSIC_LIBRARY_PATH, plan, dry_run=False)
```

### Visualizations
```python
# Create charts
plot_format_distribution(all_files)
plot_quality_distribution(all_files)
plot_top_artists(all_files, top_n=15)

# Generate report
report = generate_text_report(all_files)
```

### Playlists
```python
# Smart playlists
create_smart_playlist_by_genre(all_files, "rock", "rock_collection")
create_smart_playlist_by_year(all_files, 2000, 2009, "2000s")

# Random
create_random_playlist(all_files, count=50, playlist_name="random_50")

# Discovery
create_discovery_playlist(all_files, count=30)
```

---

## ⚠️ Important Tips

### Before Making Changes

1. **Always use dry_run=True first**
   ```python
   # Preview what will happen
   execute_organization(path, plan, dry_run=True)

   # Then execute
   execute_organization(path, plan, dry_run=False)
   ```

2. **Backup your music**
   ```bash
   # Before major reorganization
   cp -r /home/user/self-learn/music /home/user/self-learn/music_backup
   ```

3. **Start with a test folder**
   - Create a small test library first
   - Practice on 50-100 files
   - Then apply to full library

### Common Issues

**Issue:** "No metadata found"
- **Solution:** Files may not have ID3 tags. Use `batch_update_from_filename()` to auto-tag.

**Issue:** "Scan takes too long"
- **Solution:** Normal for large libraries (10,000+ files). Progress is shown every 50 files.

**Issue:** "Playlists don't work in my player"
- **Solution:** Use extended M3U8 format (`extended=True`) for better compatibility.

**Issue:** "Organization fails - target exists"
- **Solution:** You have duplicate files with same name. Resolve duplicates first with Module 02.

---

## 🎉 Next Steps

After completing your first workflows:

1. **Explore visualizations** (Module 06)
   - See trends in your collection
   - Identify gaps or quality issues
   - Export reports to share

2. **Automate maintenance**
   - Create scripts for regular tasks
   - Schedule playlist generation
   - Monitor library health

3. **Advanced features**
   - Custom smart playlist filters
   - Complex organization rules
   - Integration with media players

4. **Phase 3 modules** (optional)
   - Album art management
   - External API integration
   - File integrity validation

---

## 📚 Documentation

- **README.md** - Complete feature list
- **ENHANCEMENT_PLAN.md** - Full 8-phase roadmap
- **Each notebook** - Detailed examples and explanations

---

## 🆘 Getting Help

If you encounter issues:

1. Check the notebook's Summary section for troubleshooting
2. Review the relevant module documentation
3. Ensure all dependencies are installed
4. Check that file paths are correct
5. Try with `dry_run=True` first

---

## ✅ Success Checklist

After your first session, you should have:

- [ ] Scanned your music library
- [ ] Viewed metadata and quality statistics
- [ ] Created at least one visualization
- [ ] Generated at least one playlist
- [ ] Understood your library's organization
- [ ] Identified any quality or metadata issues

**Time to complete:** 30-60 minutes

---

**Happy organizing! 🎵**

*Last updated: 2025-11-17*
*Version: 1.5 (9 modules implemented - Phase 1, 2, and 3 complete)*
