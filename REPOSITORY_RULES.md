# Repository Organization Rules

This document defines the organizational rules and structure standards for the self-learn repository.

## Rule 1: Topic-Based Root Organization

**The root folder must only contain topic-specific folders.**

### Requirements

- ✅ **DO**: Create topic folders at root level (e.g., `data-science/`, `english/`, `malaysia-stock/`)
- ❌ **DON'T**: Create a `projects/` folder or any other generic container folders
- ✅ **DO**: Place all related content within the appropriate topic folder
- ❌ **DON'T**: Mix different topics in a single folder

### Current Topic Folders

As of 2025-11-18, the repository contains these topic folders:

1. **data-science/** - Data science learning materials (12 subcategories)
2. **english/** - English language learning resources
3. **malaysia-stock/** - Stock market technical analysis
4. **first-principle/** - First principles thinking and methodology
5. **research-methodology/** - Research methods and academic skills
6. **earn-money/** - Business and income-generating projects
7. **music/** - Music-related projects and resources
8. **n8n/** - n8n automation workflows and documentation

### Topic Folder Structure

Each topic folder should follow this internal structure:

```
topic-name/
├── notebooks/          # Educational Jupyter notebooks
├── data/               # Data files (if applicable)
│   ├── raw/            # Original unmodified data
│   ├── processed/      # Cleaned/transformed data
│   └── sample/         # Small sample datasets (<10MB)
├── docs/               # Documentation files
├── scripts/            # Utility scripts
├── tests/              # Test files
├── requirements.txt    # Python dependencies
└── README.md           # Project overview and instructions
```

### Rationale

This structure provides:

1. **Clarity**: Each topic is a clear, top-level entity
2. **Scalability**: Easy to add new topics without restructuring
3. **Navigation**: Users can immediately see all available learning topics
4. **Independence**: Each topic is self-contained with its own dependencies and documentation

### Examples

#### ✅ Good Organization

```
self-learn/
├── data-science/
│   ├── 00_tools_and_foundations/
│   └── 01_mathematics/
├── malaysia-stock/
│   ├── notebooks/
│   └── data/
└── english/
    ├── grammar/
    └── vocabulary/
```

#### ❌ Bad Organization

```
self-learn/
├── projects/                    # ❌ Generic container folder
│   ├── data-science/
│   ├── malaysia-stock/
│   └── english/
└── learning/                    # ❌ Another generic container
    └── misc/
```

## Enforcement

### When Creating New Content

1. Identify the primary topic area
2. Check if a topic folder already exists
3. If yes: Add content to the existing topic folder
4. If no: Create a new topic folder at root level
5. Never create intermediate container folders like "projects/" or "courses/"

### During Repository Maintenance

- Regularly review root-level folders to ensure compliance
- Refactor any misplaced content into appropriate topic folders
- Update documentation when new topic folders are added

## Future Rules

Additional rules may be added here as the repository evolves. Each rule should:

- Have a clear number (Rule 1, Rule 2, etc.)
- Include specific requirements with DO/DON'T examples
- Provide rationale for the rule
- Show examples of good and bad practices

---

**Last Updated**: 2025-11-18
**Version**: 1.0
