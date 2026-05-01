# Filters System Reference

Process extracted values through a pipeline of filters, inspired by Obsidian Web Clipper's 51 filters.

## Syntax

```
{{variable|filter1|filter2:"param"}}
```

Filters are chained left-to-right, each transforming the value.

---

## Core Filters

| Filter | Syntax | Function | Example |
|--------|--------|----------|---------|
| `wikilink` | `\|wikilink` | Convert to `[[wikilink]]` | `"Author" → "[[Author]]"` |
| `split` | `\|split:"delimiter"` | Split string to array | `"a, b" → ["a", "b"]` |
| `join` | `\|join:"delimiter"` | Join array to string | `["a", "b"] → "a, b"` |
| `date` | `\|date:"format"` | Format date | `"March 15, 2024" → "2024-03-15"` |
| `lower` | `\|lower` | Lowercase | `"TITLE" → "title"` |
| `upper` | `\|upper` | Uppercase | `"title" → "TITLE"` |
| `title` | `\|title` | Title case | `"hello world" → "Hello World"` |
| `trim` | `\|trim` | Remove whitespace | `"  text  " → "text"` |
| `replace` | `\|replace:"old":"new"` | Regex replace | `"hello world" → "hello-world"` |
| `first` | `\|first` | First array item | `["a", "b"] → "a"` |
| `last` | `\|last` | Last array item | `["a", "b"] → "b"` |
| `strip_tags` | `\|strip_tags` | Remove HTML tags | `"<p>text</p>" → "text"` |
| `safe_name` | `\|safe_name` | Safe filename | `"Hello World!" → "hello-world"` |

---

## Chained Filter Examples

### Multiple Authors to Wikilinks

```yaml
author: "{{author|split:', '|wikilink|join:', '}}"
# Input: "John Doe, Jane Smith"
# Output: "[[John Doe]], [[Jane Smith]]"
```

### Date Normalization

```yaml
published: "{{published|date:'YYYY-MM-DD'}}"
# Input: "March 15, 2024"
# Output: "2024-03-15"
```

### Safe Filename

```yaml
filename: "{{title|lower|replace:' ':'-'|safe_name}}"
# Input: "Hello World!"
# Output: "hello-world"
```

### Clean Content

```yaml
description: "{{description|strip_tags|trim|title}}"
# Input: "<p>  article summary  </p>"
# Output: "Article Summary"
```

---

## Type Handling

| Input Type | Filter | Output Type |
|------------|--------|-------------|
| string | `split` | array |
| array | `join` | string |
| array | `first`, `last` | string |
| string | `wikilink` | string |
| string | `lower`, `upper`, `title` | string |
| string | `trim`, `strip_tags` | string |

---

## Processing Order

1. Extract variable value from page
2. Apply filters left-to-right
3. Handle type conversions automatically
4. Return final value for frontmatter

---

## Implementation Note

Filters are applied by AI during content analysis. No external code execution is needed - the AI interprets the filter syntax and applies transformations directly.