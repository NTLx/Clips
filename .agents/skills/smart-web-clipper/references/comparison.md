# Feature Comparison: Smart Web Clipper vs Obsidian Web Clipper

## Summary

| Category | Web Clipper | This Skill | Advantage |
|----------|------------|------------|-----------|
| **Variable Coverage** | 100% | 100% | ✅ Full parity achieved |
| **Filters Coverage** | 51 filters | 13 core | ✅ Essential filters implemented |
| **Dynamic Content** | Limited | Full JS | ✅ Better SPA support |
| **AI Analysis** | Optional (Interpreter) | Built-in | ✅ Always available |
| **Knowledge Integration** | Manual wikilinks | Auto-linking | ✅ Wiki-aware |
| **Batch Processing** | Manual | Team mode | ✅ Parallel clipping |
| **Quality Control** | Manual review | Auto assessment | ✅ Credibility check |

---

## Detailed Comparison

### Preset Variables

| Variable | Web Clipper | This Skill |
|----------|------------|------------|
| `{{title}}` | ✅ | ✅ |
| `{{author}}` | ✅ | ✅ + wikilink detection |
| `{{content}}` | ✅ Markdown | ✅ Markdown |
| `{{contentHtml}}` | ✅ HTML | ✅ CDP raw HTML |
| `{{fullHtml}}` | ✅ Full page | ✅ `outerHTML` |
| `{{description}}` | ✅ | ✅ |
| `{{domain}}` | ✅ | ✅ |
| `{{url}}` | ✅ | ✅ + tracking cleanup |
| `{{published}}` | ✅ | ✅ + date normalization |
| `{{date}}` | ✅ Current | ✅ Current |
| `{{time}}` | ✅ Datetime | ✅ ISO format |
| `{{site}}` | ✅ | ✅ Extracted |
| `{{favicon}}` | ✅ | ✅ Extracted |
| `{{image}}` | ✅ | ✅ og:image + fallback |
| `{{words}}` | ✅ | ✅ AI calculated |
| `{{highlights}}` | ✅ | ✅ CDP selection |
| `{{selection}}` | ✅ Markdown | ✅ Markdown |
| `{{selectionHtml}}` | ✅ HTML | ✅ HTML |

### Meta Variables

| Feature | Web Clipper | This Skill |
|---------|------------|------------|
| `{{meta:name:X}}` | ✅ | ✅ |
| `{{meta:property:X}}` | ✅ | ✅ + all OG tags |

### Selector Variables

| Feature | Web Clipper | This Skill |
|---------|------------|------------|
| `{{selector:X}}` | ✅ Text | ✅ |
| `{{selector:X?attr}}` | ✅ Attribute | ✅ |
| `{{selectorHtml:X}}` | ✅ HTML | ✅ |

### Schema.org Variables

| Feature | Web Clipper | This Skill |
|---------|------------|------------|
| `{{schema:@Type:key}}` | ✅ | ✅ |
| `{{schema:key}}` (shorthand) | ✅ | ✅ |
| Nested/array access | ✅ | ✅ |

### Prompt Variables

| Feature | Web Clipper | This Skill |
|---------|------------|------------|
| Flexible prompts | ✅ User-defined | ✅ Pre-configured |
| Provider choice | ✅ Configurable | ✅ Claude (built-in) |
| Cost considerations | ⚠️ API usage | ✅ No extra cost |

### Filters System

| Feature | Web Clipper | This Skill |
|---------|------------|------------|
| `wikilink` | ✅ | ✅ Auto entity linking |
| `split` / `join` | ✅ | ✅ Array handling |
| `date` formatting | ✅ | ✅ YYYY-MM-DD normalization |
| `lower` / `upper` / `title` | ✅ | ✅ Case transforms |
| `trim` | ✅ | ✅ Whitespace cleanup |
| `replace` | ✅ Regex | ✅ Regex support |
| `first` / `last` | ✅ | ✅ Array selection |
| `strip_tags` | ✅ | ✅ HTML cleanup |
| `safe_name` | ✅ | ✅ Filename sanitization |
| Chained filters | ✅ Pipe syntax | ✅ `{{var|f1|f2:"p"}}` |

### AI-Exclusive Features

| Feature | Web Clipper | This Skill |
|---------|------------|------------|
| Static extraction | ✅ Template variables | ✅ CDP snapshot |
| Dynamic content | ❌ Limited | ✅ Full JS rendering |
| Content understanding | ❌ No | ✅ AI semantic analysis |
| Duplicate detection | ❌ No | ✅ Compare with existing |
| Knowledge linking | ❌ No | ✅ Auto wikilinks to wiki |
| Quality assessment | ❌ No | ✅ Relevance + credibility |
| Entity extraction | ❌ No | ✅ Candidate suggestions |
| Stance analysis | ❌ No | ✅ Objectivity check |
| Link evaluation | ❌ No | ✅ Worth clipping判断 |
| Crawl depth decision | ❌ Fixed | ✅ AI dynamic judgment |
| Batch clipping | ❌ Manual | ✅ Team mode parallel |
| Author wikilink | ⚠️ Template config | ✅ Auto entity detection |
| Updated date | ⚠️ Template config | ✅ Auto extraction |
| Changes/history link | ❌ No | ✅ Preserved for evolving content |
| Content mode | ❌ Fixed | ✅ Preserve vs Synthesize |

---

## Filters Implementation Note

This skill implements 13 core filters that cover the most common data transformation needs:
- wikilink conversion
- array manipulation
- date formatting
- case transforms
- text cleanup

The 51 filters in Web Clipper include additional specialized filters for URL encoding, math operations, and advanced text processing - these can be added as needed based on use cases.