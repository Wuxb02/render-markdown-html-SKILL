# render-markdown-html

[English](./readme-en.md) | 中文

> Markdown ↔ HTML 双向转换技能 — 为 Claude Code 提供高质量文档渲染与回写能力。

## 功能

| 能力 | 说明 |
| --- | --- |
| **Markdown → HTML** | 将 Markdown 渲染为结构清晰、适合阅读的单文件 HTML |
| **参数可编辑** | 将 HTML 中的颜色、间距、布局等参数暴露为可视化控件 |
| **Write Back** | 为每个可配置项提供明确的「回写」按钮，修改可落回 Markdown |
| **HTML → Markdown** | 从 HTML 中恢复语义结构，生成干净的 Markdown 源文件 |
| **语言一致** | 自动匹配源文件语言，中文正文中的 UI 标签也使用中文 |

## 使用场景

- 用户需要将 `.md` 文件导出为可浏览的 HTML 页面
- 用户希望在 HTML 中直接调整主题色、间距、密度等参数
- 用户需要从 HTML 恢复 Markdown 以继续编辑
- 用户想要一份更适合人类阅读的长文档展示

## 快速开始

```bash
# 渲染 Markdown 为 HTML
/render-markdown-html docs/summary.md

# 从 HTML 恢复 Markdown
/html-to-md report.html
```

## 项目结构

```text
render-markdown-html/
├── SKILL.md                        # 技能定义与规则说明
├── scripts/
│   ├── md_to_html.py               # Markdown 输入解析
│   └── html_to_md.py               # HTML 输入解析
├── references/
│   ├── template-library.md         # 视觉与交互模式参考
│   └── examples/
│       ├── 01-document-review.html       # 长文档审阅布局
│       ├── 02-configurable-card.html     # 可配置卡片
│       └── 03-editorial-split-view.html  # 编辑器分屏视图
├── readme.md                       # 中文说明（本文件）
└── readme-en.md                    # English README
```

## 设计风格

采用沉稳的编辑器风格，而非花哨的落地页：

- 低饱和度配色 — 象牙白 / 石板灰 / 陶土棕 / 橄榄绿
- 细边框、克制阴影、紧凑圆角
- 标题用衬线体，正文用无衬线体
- 侧边导航 + 粘性工具栏 + 分屏预览
- 明确的状态反馈：已保存 / 未保存 / 已回写 / 已导出

## 相关文档

- [Skill Spec](./SKILL.md)
- [Template Library](./references/template-library.md)

## 致谢

- Thariq 的[原始推文](https://x.com/trq212/status/2052809885763747935)启发了本技能的设计思路
- [HTML 示例站](https://thariqs.github.io/html-effectiveness/)提供了视觉与交互参考
