## Main Copilot features

- **Inline code completions and chat in IDE**: In VS Code, Visual Studio, JetBrains, etc., Copilot suggests code as you type and supports conversational chat for explanations, refactors, and generating tests. You can select code or files and ask it to explain, refactor, or document them.[2][5][6][7]
- **Edit mode and agent mode**: Edit mode lets you constrain which files it can touch and iteratively apply precise edits, while agent mode allows Copilot to autonomously choose files, propose diffs, run commands, and iterate until a task is done (for example, implementing an endpoint plus tests).[8][1]
- **Code review and PR summaries**: Copilot can do AI-generated code review suggestions and generate pull request summaries highlighting what changed and where reviewers should focus.[1]
- **Copilot CLI and terminal integration**: In GitHub CLI and Windows Terminal, Copilot can map project structure, install dependencies, explain commands, and run local edit/debug/refactor loops without leaving the terminal.[3][9]
- **Copilot Spaces and knowledge bases**: You can organize code, specs, and docs into “Spaces” or enterprise knowledge bases that ground Copilot’s answers in your org’s specific repositories and documentation.[5][1]
- **Cross-surface availability**: Copilot is available in IDEs, GitHub.com (issues, PRs, repos), GitHub Desktop for commit message generation, GitHub Mobile, and the command line.[5][1]

## Newest / recently shipped features

- **Agent mode as a coding agent**: GitHub calls out an “agent mode” where Copilot works asynchronously as a coding agent to handle multi-step tasks like refactoring, improving test coverage, and fixing defects across files; it can coordinate with other agents over the dev lifecycle.[4][8][1]
- **App modernization capabilities**: New Java and .NET app modernization features let Copilot assess large legacy apps and then autonomously generate and execute upgrade plans (e.g., framework upgrades, dependency updates, remediation), with summaries and checkpoints.[4]
- **Expanded Spaces / knowledge context**: Spaces and enterprise knowledge bases are newer mechanisms to centralize relevant content (code, specs, docs) and use it as context for Copilot’s responses, which is especially important in larger organizations.[1][5]
- **Deeper Visual Studio 2026 integration**: Visual Studio 2026 ships with enhanced Copilot experiences including a cloud coding agent toggle to delegate repetitive UI cleanups, refactors, and multi-file edits directly from the IDE.[10]
- **CLI: local edit/debug loops and MCP**: Recent “what’s new” updates highlight CLI features like editing, debugging, refactoring code locally via Copilot CLI, and including GitHub MCP with extension to more MCP servers for richer contextual tools.[3]
- **Documentation and explanation workflows**: GitHub’s own training and blogs emphasize Copilot’s capabilities to explain legacy code, generate inline comments, write README/docs, and help document complex systems, now available even in the free tier.[6][7]

## How these features improve software development

- **Faster implementation and refactoring**: Inline completions, edit mode, and agent mode reduce boilerplate and repetitive edits, letting developers request higher-level changes (“implement this endpoint plus tests”) and approve diffs instead of hand-writing every line. Empirical reports and GitHub case studies (for example, their October 2025 workflow overview) describe measurable productivity gains from offloading routine edits and refactors to Copilot.[9][8][1]
- **Better code quality and maintainability**: Code review suggestions, PR summaries, and modernization features help identify issues, improve test coverage, and guide safe upgrades of legacy .NET/Java apps, which reduces defects and technical debt over time. Documentation/explanation features make it easier to understand and document legacy systems, improving long-term maintainability for teams inheriting old codebases.[7][6][4][1]
- **Improved onboarding and knowledge transfer**: Spaces/knowledge bases let Copilot answer questions using your specific repos and docs, supporting new team members who can query architecture or module behavior in natural language instead of manually hunting through wikis. GitHub’s materials explicitly position these capabilities as a way to centralize context and reduce ramp-up time for developers joining complex projects.[9][5][1]
- **Reduced context-switching across tools**: With IDE integration, GitHub.com integration, Desktop commit message generation, mobile chat, and CLI/terminal workflows, developers can stay in their primary environment while Copilot handles generation, explanation, and editing tasks. This continuous assistance across surfaces is highlighted as a key reason why teams see smoother workflows and fewer interruptions.[3][5][9][1]

If you’d like, I can map these capabilities specifically against your Marcus/agent-infrastructure workflow (e.g., how to combine Copilot agent mode + your own agents for greenfield feature work or legacy modernization pipelines).

Sources
[1] GitHub Copilot features https://docs.github.com/en/copilot/get-started/features
[2] GitHub Copilot · Your AI pair programmer https://github.com/features/copilot
[3] See what's new with GitHub Copilot https://github.com/features/copilot/whats-new
[4] Build 2025: Big Updates for GitHub Copilot, Open Source ... https://www.thurrott.com/a-i/github-copilot/321127/build-2025-big-updates-for-github-copilot-open-source-implementation-in-visual-studio-code
[5] What is GitHub Copilot? https://docs.github.com/en/copilot/get-started/what-is-github-copilot
[6] Generate Documentation Using GitHub Copilot Tools - Training https://learn.microsoft.com/en-us/training/modules/generate-documentation-using-github-copilot-tools/
[7] Documenting and explaining legacy code with GitHub Copilot https://github.blog/ai-and-ml/github-copilot/documenting-and-explaining-legacy-code-with-github-copilot-tips-and-examples/
[8] GitHub Copilot Master Guide 2026: The Ultimate AI Coding Handbook https://trendminds.in/github-copilot-master-guide-2026-the-ultimate-ai-coding-handbook/
[9] GitHub Copilot: Transforming Development Workflows as of October ... https://www.oreateai.com/blog/github-copilot-transforming-development-workflows-as-of-october-2025/401099862d6eac772e360bbdc2b5c1bf
[10] GitHub Copilot in Visual Studio — November update https://github.blog/changelog/2025-12-03-github-copilot-in-visual-studio-november-update/
[11] Available features for Visual Studio 2026 : r/GithubCopilot - Reddit https://www.reddit.com/r/GithubCopilot/comments/1qboyfy/available_features_for_visual_studio_2026/
[12] GitHub Copilot in 2026 | The AI That Changed My Coding Life ... https://www.linkedin.com/pulse/github-copilot-2026-ai-changed-my-coding-lifeforever-iqbal-hussain-oihgf
[13] What's New in Copilot Studio: November 2025 Updates and Features https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/whats-new-in-microsoft-copilot-studio-november-2025/
[14] What's new for Copilot - December 2025 - YouTube https://www.youtube.com/watch?v=uPqJkJUCcRA
[15] GitHub's December 2025 - January 2026: The Ships That Matter https://dev.to/andreagriffiths11/githubs-december-2025-january-2026-the-ships-that-matter-2bgi
