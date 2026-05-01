# Edge Cases Reference

Detailed handling for various edge cases in web clipping.

## Access Issues

| Situation | Handling |
|-----------|----------|
| Paywall / Login required | Notify user, skip clipping |
| 404 / Not found | Try archive.org, notify if failed |
| Rate limited | Wait and retry, or notify user |
| Certificate error | Warn user, ask whether to proceed |

## Content Types

| Situation | Handling |
|-----------|----------|
| Video-heavy page | Extract transcript if available, otherwise capture title and description |
| PDF document | Download to `00-raw/pdf-docs/` or user-specified path |
| Non-English content | Detect language, add `language:` to frontmatter |
| Image gallery | Extract image URLs, consider downloading |
| Audio/Podcast | Extract show notes, title, duration |

## Technical Challenges

| Situation | Handling |
|-----------|----------|
| SPA with lazy loading | Scroll, wait, re-snapshot |
| Infinite scroll | Capture first N items (default: 50), notify user |
| Cookie banner | Attempt to dismiss, or extract visible content only |
| Anti-bot protection | May fail gracefully, notify user |

## Environment Issues

| Situation | Handling |
|-----------|----------|
| **No Obsidian CLI** | Use direct file write with Obsidian Markdown compliance |
| **Headless server** | Write to `$HOME/clippings/` or user-specified directory |
| **User specifies custom path** | Honor user's path preference over defaults |
| **Write permission denied** | Try fallback locations, notify user |

## Content Quality

| Situation | Handling |
|-----------|----------|
| **Duplicate detected** | Alert user, show existing clipping, ask whether to proceed |
| **Low credibility content** | Add `credibility: flagged` with reason, warn user |
| **Promotional/soft ad** | Mark `stance: promotional`, suggest careful handling |
| **High relevance but no entities** | Suggest creating new entities during compile |
| **Links to existing wiki pages** | Auto-add wikilinks to related entities/topics |

## Author Handling

| Situation | Handling |
|-----------|----------|
| **Author entity exists** | Use `[[Author Name]]` wikilink format in frontmatter |
| **Author entity not found** | Use plain text, mark as candidate for entity creation |
| **Multiple authors** | Use `split` filter: `{{author|split:", "|wikilink}}` |
| **No author found** | Skip author field, note in AI metadata |
| **Corporate author** | Use organization name as author |

## Date Handling

| Situation | Handling |
|-----------|----------|
| **Page has Last modified date** | Extract to `updated:` field in frontmatter |
| **No publication date** | Try Schema.org, meta tags, visible text in order |
| **Ambiguous date format** | Use AI to parse and normalize to YYYY-MM-DD |

## Evolving Content

| Situation | Handling |
|-----------|----------|
| **Page has changes/history link** | Add `changes_url:` to frontmatter for reference |
| **Continuously updated guide** | Preserve original structure, add version tracking |
| **Documentation with versions** | Note the version captured in frontmatter |

## Content Mode Selection

| Situation | Recommended Mode |
|-----------|-----------------|
| Technical documentation | **preserve** - Keep section hierarchy |
| Tutorial/guide | **preserve** - Maintain step order |
| Opinion/editorial | **synthesize** - AI reorganizes with highlights |
| News article | **synthesize** - Quick understanding focus |
| Reference material | **preserve** - Original structure important |
| Essay | **synthesize** - Highlight key arguments |

## Batch Clipping

| Situation | Handling |
|-----------|----------|
| 1-3 URLs | Process sequentially or parallel (Team mode optional) |
| 4-10 URLs | Use Team mode with 3-5 concurrent agents |
| 10+ URLs | Batch into groups of 5-10, use Team mode, report progress |
| Mixed content types | Each agent handles its own content type detection |

## Error Recovery

| Situation | Handling |
|-----------|----------|
| Navigation timeout | Retry once, then notify user |
| Snapshot fails | Re-navigate and retry |
| Write fails | Try fallback location, check permissions |
| Partial content | Save what was captured, note incomplete status |