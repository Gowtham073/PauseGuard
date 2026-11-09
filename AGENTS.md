# Multi-Model Agent Guidelines

## Role Assignments
- **Architecture & Planning:** Assigned to models with High reasoning (e.g., Nemotron / GPT OSS 120B) for breaking down complex requirements.
- **Implementation & Coding:** Assigned to fast models (e.g., GLM-5.3 Flash / DeepSeek V4.1 Flash) for writing boilerplate and functional components.
- **Independent Review:** Use a secondary model to review code diffs before committing.

## Safety & Workflow Rules
1. **Branch Hygiene:** Always create a new Git branch (`git checkout -b feature/my-feature`) before allowing an agent to make major modifications.
2. **File Isolation:** Do not let concurrent agents modify the same file simultaneously. Review all diffs carefully.
3. **No Destructive Commands:** Terminal commands that alter system state or force-overwrite files require explicit user approval.