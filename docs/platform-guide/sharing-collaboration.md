# Sharing and Collaboration --- Working with Teams

Simba supports collaborative workflows through model sharing, portfolio sharing, team-based projects, and role-based access control. This guide covers how to organize your work and collaborate with colleagues.

---

## Project Organization

Projects are containers for organizing related models within your workspace.

### Default Project

Every user has a default project. Models created without specifying a project are placed here automatically.

### Creating Projects

To organize your work:

1. Create a new project from the Warehouse or project management interface.
2. Name it to reflect its purpose (e.g., "UK Q1 2026 Analysis", "Client: Acme Corp", "Brand Launch Campaign").
3. Assign models to the project during creation or move existing models into it.

Projects can be shared with teams for collaborative access (see Team Management below).

---

## Model Sharing

Share individual models with other Simba users to enable collaborative analysis.

### Sharing a Model

1. Open the model you want to share from the Warehouse or Active Model page.
2. Click the **Share** action.
3. Enter the email address or username of the person you want to share with.
4. The model is now accessible to the recipient.

### Managing Shares

- **View shares**: See who has access to each model via the shares list.
- **Remove access**: Revoke sharing for specific users by removing their share.
- **Private vs shared views**: Your "My Models" section shows models you own. The "Shared with me" section shows models others have shared with you.

---

## Portfolio Sharing

Share entire portfolios (collections of linked models) with other users.

### Sharing a Portfolio

1. Open the portfolio from the Warehouse Portfolios tab.
2. Click the **Share** action.
3. Enter the recipient's details.
4. Portfolio sharing grants the recipient access to the portfolio and its linked models.

### Managing Portfolio Shares

- View and manage portfolio share permissions independently of individual model shares.
- Private and shared portfolio views work the same way as model views.

---

## Team Management

Teams provide a structured way to manage groups of collaborators.

### Creating a Team

1. Navigate to **Settings > Team Management**.
2. Click **Create Team**.
3. Name your team (e.g., "Media Planning", "Analytics", "Client Services").

### Managing Team Members

- **Add members**: Invite users by email. They will receive an invitation to join the team.
- **Remove members**: Remove users who no longer need access.
- **Assign roles**: Set appropriate permission levels for each team member.

### Sharing with Teams

Instead of sharing models or projects with individual users, you can share with an entire team:

- Share a project with a team to grant all team members access to the models within that project.
- When team membership changes, access is automatically updated.

---

## Roles and Permissions

Simba uses role-based access control:

| Role | Capabilities |
|---|---|
| **Owner** | Full control --- manage billing, team, settings, and all modeling features. |
| **Admin** | Manage team members, data, and models. Cannot modify billing. |
| **Analyst** | Upload data, configure and run models, create scenarios, run optimizations. Cannot manage team or settings. |
| **Viewer** | View results, reports, and dashboards. Cannot modify data or models. |

---

## Best Practices

- **Use projects to organize before sharing** --- group related models into a project, then share the project rather than individual models.
- **Share at the portfolio level** for cross-brand analysis --- this ensures collaborators can see the full picture.
- **Use teams for recurring collaborations** --- agency-client relationships, cross-functional teams, and department-level access are best managed through teams.
- **Review shares periodically** --- remove access for users who no longer need it.

---

## Next Steps

- [Account Setup](../getting-started/account-setup.md) --- Plans, workspaces, and initial team configuration
- [Portfolio Analysis](./portfolio-analysis.md) --- Collaborative portfolio workflows
- [Exports and Reporting](./exports-reporting.md) --- Share results outside the platform
