# Variables Extraction Reference

Detailed documentation for all variable types supported by Smart Web Clipper.

## 1. Preset Variables (预设变量)

| Variable | Description | Extraction Method |
|----------|-------------|-------------------|
| `{{title}}` | Page title | `<title>`, `<h1>`, AI cleanup |
| `{{author}}` | Author name | Meta tags, byline, AI inference |
| `{{content}}` | Main content (Markdown) | CDP snapshot → Markdown conversion |
| `{{contentHtml}}` | Main content (HTML) | CDP snapshot raw HTML |
| `{{fullHtml}}` | Full page HTML | `document.documentElement.outerHTML` |
| `{{description}}` | Description/excerpt | `<meta name="description">`, first paragraph |
| `{{domain}}` | Domain name | `window.location.hostname` |
| `{{url}}` | Current URL | `window.location.href` (cleaned) |
| `{{published}}` | Published date | Meta tags, visible date, Schema.org |
| `{{date}}` | Current date | System date (YYYY-MM-DD) |
| `{{time}}` | Current datetime | System datetime (ISO format) |
| `{{site}}` | Site name/publisher | `<meta property="og:site_name">`, logo alt text |
| `{{favicon}}` | Favicon URL | `<link rel="icon">`, `/favicon.ico` |
| `{{image}}` | Social share image | `<meta property="og:image">`, first large image |
| `{{words}}` | Word count | Content word count (AI-calculated) |
| `{{highlights}}` | User highlights | CDP highlight extraction with timestamps |
| `{{selection}}` | Selected text (Markdown) | `window.getSelection()` → Markdown |
| `{{selectionHtml}}` | Selected text (HTML) | `window.getSelection()` → HTML |

**Implementation Notes**:
- `{{highlights}}`: Requires user to highlight text before clipping. Use `evaluate_script` to extract selection ranges.
- `{{selection}}`: If user has selected text, prioritize that over full content.
- `{{site}}`: Often confused with `domain`. Site is the brand name (e.g., "GitHub" vs "github.com").

---

## 2. Meta Variables (元变量)

Extract from `<meta>` elements including Open Graph:

| Syntax | Example | Description |
|--------|---------|-------------|
| `{{meta:name:X}}` | `{{meta:name:description}}` | Meta name tag content |
| `{{meta:property:X}}` | `{{meta:property:og:title}}` | Meta property tag content |

### Common Open Graph Variables

| Variable | Meta Tag | Typical Value |
|----------|----------|---------------|
| `og:title` | `<meta property="og:title">` | Share preview title |
| `og:description` | `<meta property="og:description">` | Share preview description |
| `og:image` | `<meta property="og:image">` | Share preview image |
| `og:site_name` | `<meta property="og:site_name">` | Site/brand name |
| `og:type` | `<meta property="og:type">` | Content type (article, video) |
| `og:url` | `<meta property="og:url">` | Canonical URL |
| `article:published_time` | `<meta property="article:published_time">` | Published datetime |
| `article:modified_time` | `<meta property="article:modified_time">` | Modified datetime |
| `article:author` | `<meta property="article:author">` | Author profile URL |

### Implementation

```javascript
// Extract meta content via CDP evaluate_script
function getMetaByName(name) {
  const meta = document.querySelector(`meta[name="${name}"]`);
  return meta ? meta.content : null;
}

function getMetaByProperty(property) {
  const meta = document.querySelector(`meta[property="${property}"]`);
  return meta ? meta.content : null;
}
```

---

## 3. Selector Variables (选择器变量)

Extract content using CSS selectors:

| Syntax | Example | Description |
|--------|---------|-------------|
| `{{selector:X}}` | `{{selector:.author}}` | Text content of matching elements |
| `{{selector:X?attr}}` | `{{selector:img.hero?src}}` | Attribute value of matching element |
| `{{selectorHtml:X}}` | `{{selectorHtml:article}}` | HTML content of matching elements |

### Examples

| Selector | Purpose | Returns |
|----------|---------|---------|
| `{{selector:h1}}` | Main heading | Text content |
| `{{selector:.byline}}` | Author byline | Text content |
| `{{selector:time?datetime}}` | Publication datetime | ISO datetime attribute |
| `{{selector:a.main-link?href}}` | Main link URL | href attribute |
| `{{selector:img.featured?src}}` | Featured image URL | src attribute |

### Implementation

```javascript
function extractSelector(selector, attribute = null) {
  const elements = document.querySelectorAll(selector);
  const results = Array.from(elements).map(el => {
    if (attribute) return el.getAttribute(attribute);
    return el.textContent.trim();
  });
  return results.length === 1 ? results[0] : results;
}
```

### Use Cases

- **Site-specific templates**: Create templates that work on specific sites with known HTML structure
- **Precise extraction**: When meta tags aren't available, extract from visible elements
- **Multiple values**: Returns array when multiple elements match

---

## 4. Schema.org Variables (结构化变量)

Extract from JSON-LD structured data:

| Syntax | Example | Description |
|--------|---------|-------------|
| `{{schema:@Type:key}}` | `{{schema:@Article:author}}` | Property from specific schema type |
| `{{schema:@Type:parent.child}}` | `{{schema:@Article:author.name}}` | Nested property |
| `{{schema:@Type:array[*].prop}}` | `{{schema:@Article:author[*].name}}` | All items in array |
| `{{schema:key}}` (shorthand) | `{{schema:author}}` | First matching property |

### Common Schema Types

| Type | Common Properties |
|------|-------------------|
| `@Article` | headline, author, datePublished, dateModified, image, publisher |
| `@BlogPosting` | headline, author, datePublished, wordCount |
| `@NewsArticle` | headline, datePublished, author, publisher |
| `@Product` | name, price, brand, description, image |
| `@Person` | name, url, jobTitle, sameAs |
| `@Organization` | name, url, logo, sameAs |

### Implementation

```javascript
function extractSchema(type = null, path) {
  const scripts = document.querySelectorAll('script[type="application/ld+json"]');
  for (const script of scripts) {
    try {
      const data = JSON.parse(script.textContent);
      if (type && data['@type'] !== type) continue;
      
      const keys = path.split(/[.\[\]]+/).filter(Boolean);
      let value = data;
      for (const key of keys) {
        if (key === '*') continue;
        value = value?.[parseInt(key) ?? key];
      }
      return value;
    } catch (e) { continue; }
  }
  return null;
}
```

---

## 5. Prompt Variables (AI增强变量)

AI-powered extraction using natural language:

| Feature | Description | Advantage |
|---------|-------------|-----------|
| **AI Summary** | Generate concise summary | Better than meta description |
| **AI Tags** | Suggest relevant tags | More specific than categories |
| **AI Entities** | Extract key concepts | Identify wiki page candidates |
| **AI Stance** | Detect author position | Objectivity assessment |
| **AI Credibility** | Trust level evaluation | Quality filtering |
| **AI Reading Time** | Estimated duration | Complexity-adjusted |
| **AI Language** | Detect language | Non-English content flagging |

### Comparison with Web Clipper's Prompt Variables

| Aspect | Web Clipper | This Skill |
|--------|------------|------------|
| Syntax | `{{"prompt text"}}` | AI analysis built into workflow |
| Provider | Configurable LLM | Claude (current model) |
| Flexibility | User-defined prompts | Pre-configured analysis |
| Cost | API usage | Built-in (no extra cost) |
| Privacy | External API | Local processing |

---

## 6. AI Content Analysis

Additional AI-enhanced fields extracted during content analysis:

| Field | Source | AI Enhancement |
|-------|--------|---------------|
| **title** | `<title>`, `<h1>` | Clean up, remove site suffix |
| **author** | `meta author`, byline | Infer from content patterns |
| **published** | `meta date`, visible date | Normalize to YYYY-MM-DD |
| **updated** | `Last modified`, `updated` meta | Extract modification date if available |
| **source** | Current URL | Clean tracking parameters |
| **domain** | Hostname | Extract for categorization |
| **tags** | Content analysis | AI-suggested based on content |
| **category** | Domain knowledge | Map to knowledge base categories |
| **summary** | Full content analysis | AI-generated core points |
| **changes_url** | Page footer, version link | Extract history link for evolving content |

### Author Wikilink Detection (HIGH PRIORITY)

```
1. Extract author name from page
2. Convert to entity filename: "Author Name" → "Author-Name.md"
3. Check if 10-wiki/entities/{Author-Name}.md exists
4. If exists → author: ["[[Author Name]]"] (wikilink format)
5. If not exists → author: ["Author Name"] (plain text only)
6. After clipping, suggest creating entity page
```

### Date Extraction Priority

| Priority | Source | Example |
|----------|--------|---------|
| 1 | Schema.org `dateModified` | `<meta itemprop="dateModified">` |
| 2 | Visible "Last modified" text | `Last modified: 16th March 2026` |
| 3 | `updated` meta tag | `<meta name="updated" content="2026-03-16">` |
| 4 | Git commit date (if repo visible) | GitHub page commit date |

### Changes/History Link Detection

For continuously updated articles:
- Text like "N changes", "View history", "Changelog"
- Links to `/changes/`, `/history/`, `/changelog/`
- Store in `changes_url` field for reference