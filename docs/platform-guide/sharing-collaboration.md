# Sharing and Collaboration --- Working with Teams

Simba supports collaborative workflows through model sharing, portfolio sharing, and team management. Organize your work into projects, share models or portfolios with individuals or teams, and manage team membership from the Teams page.

---

## Projects

Projects are organizational containers for grouping related models within your account.

**Creating a project:**
1. Create a new project from the Warehouse interface.
2. Name it to reflect its purpose (e.g., "UK Q1 2026 Analysis", "Client: Acme Corp", "Brand Launch Campaign").
3. Assign models to the project during creation or move existing models into it.

Every user has a default project. Models created without specifying a project are placed here automatically.

> **Note**: Projects themselves cannot be shared. To collaborate, share individual models or portfolios (see below).

---

## Model Sharing

Share individual models with other Simba users to enable collaborative analysis. You can share with a specific user by email or with an entire team.

### Sharing a Model

1. Open the model from the Warehouse or Active Model page.
2. Click the **Share** action.
3. Enter the **email address** of the person you want to share with, or select a **team** to share with all team members.
4. The model becomes accessible to the recipient(s).

> **Important**: The user you're sharing with must already have a Simba account. There is no invitation link system — users must sign up first, then you can share with them by email.

### Managing Shares

- **View shares**: See who has access to each model via the shares list.
- **Remove access**: Revoke sharing for specific users by removing their share.
- **Private vs shared views**: Your "My Models" section shows models you own. The "Shared with me" section shows models others have shared with you.

---

## Portfolio Sharing

Share entire [portfolios](./portfolio-analysis.md) (collections of linked models) with other users or teams. Portfolio sharing is independent of individual model sharing.

### Sharing a Portfolio

1. Open the portfolio from the Warehouse Portfolios tab.
2. Click the **Share** action.
3. Enter the recipient's email or select a team.
4. The portfolio and its analysis views become accessible to the recipient(s).

### Managing Portfolio Shares

- View and manage portfolio shares independently of individual model shares.
- Private and shared portfolio views work the same way as model views.

---

## Team Management

Teams provide a structured way to manage groups of collaborators. Navigate to the **Teams** page from the dashboard sidebar.

### Creating a Team

1. Navigate to the **Teams** page.
2. Click **Create Team**.
3. Name your team (e.g., "Media Planning", "Analytics", "Client Services").

The user who creates the team is the **owner**.

### Managing Team Members

- **Add members**: Add users by their email address. The user must already have a Simba account.
- **Remove members**: Remove users who no longer need access. Only the team owner can add or remove members.

> **Note**: Teams have two roles: **owner** (creator, can manage members and delete the team) and **member** (can access models/portfolios shared with the team). There are no additional permission levels.

### Sharing with Teams

Instead of sharing models or portfolios with individual users one by one, share with an entire team:

- Share a model or portfolio with a team to grant all team members access.
- When team membership changes, access is automatically updated — new members gain access, removed members lose it.

---

## Account Security

### Two-Factor Authentication (2FA)

Enable 2FA from **Profile > Two-Factor Authentication** tab for an additional layer of account security.

### Single Sign-On (SSO)

Simba supports OAuth sign-in with:
- **Google** accounts
- **Microsoft** accounts (Azure AD)

SSO simplifies access management for organizations that use Google Workspace or Microsoft 365.

---

## Best Practices

- **Share at the model or portfolio level** --- projects are for your own organization; sharing happens on individual models and portfolios.
- **Use teams for recurring collaborations** --- agency-client relationships, cross-functional teams, and department-level access are best managed through teams rather than individual shares.
- **Share portfolios for cross-brand analysis** --- this ensures collaborators can see the full [portfolio analysis](./portfolio-analysis.md) view.
- **Review shares periodically** --- remove access for users who no longer need it.
- **Enable 2FA** --- especially for accounts with access to sensitive marketing data.

---

## Next Steps

**Platform guides:**
- [Portfolio Analysis](./portfolio-analysis.md) --- Collaborative portfolio workflows
- [Exports and Reporting](./exports-reporting.md) --- Share results outside the platform
- [Model Configuration](./model-configuration.md) --- Model setup and management

**Getting started:**
- [Account Setup](../getting-started/account-setup.md) --- Registration and initial configuration
