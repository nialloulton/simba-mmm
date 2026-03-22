# Account Setup — Registration, Plans, and Workspace Configuration

This guide covers everything you need to get your Simba account up and running: creating your account, understanding the available plans, configuring your workspace, and setting up team collaboration.

---

## Creating Your Account

### Sign up

1. Visit [getsimba.ai](https://getsimba.ai) and click **Start Free Trial**.
2. Enter your name, email address, and create a password — or sign up using Google SSO.
3. Verify your email address by clicking the confirmation link sent to your inbox.
4. You will be taken to your new workspace, ready to upload data and start modeling.

### The 14-day free trial

Every new account starts with a **14-day Sandbox trial**. During this period, you have access to core Simba features so you can evaluate the platform with your own data. No credit card is required to begin.

The Sandbox trial includes:

- Data upload and the AI Data Auditor
- Model configuration with smart defaults
- Model execution and results interpretation
- Basic scenario planning

At the end of your trial, you can choose a paid plan to continue. Your data and model configurations are preserved when you upgrade.

---

## Choosing a Plan

Simba offers several plans designed for different team sizes and use cases. Below is an overview of each tier by features and audience. For current pricing, visit [getsimba.ai](https://getsimba.ai).

### Sandbox (Free Trial)

**Best for:** Evaluating Simba before committing.

- 14-day full-feature trial
- Single workspace
- Core modeling features
- Smart defaults
- Basic scenario planning
- No credit card required

### Analyst

**Best for:** Individual analysts and small marketing teams running a single brand.

- Single workspace
- Full AI Data Auditor
- Incremental Measurement with complete model configuration (priors, adstock, saturation)
- Scenario Planning
- Budget Intelligence optimization
- Email support

### Pro (Best Value)

**Best for:** Growing marketing teams and performance-focused brands that need the full platform.

- Everything in Analyst
- Multiple model versions and comparison
- Advanced model diagnostics
- Extended data history support
- Priority support
- This plan offers the strongest balance of features and value for most marketing teams

### Scale

**Best for:** Agencies and consultancies managing multiple clients.

- Everything in Pro
- Multi-workspace support for managing separate client environments
- Team collaboration with role-based access
- Cross-client reporting capabilities
- Dedicated onboarding support
- Agency-specific workflow features

### Enterprise

**Best for:** Large organizations with advanced security, compliance, and customization requirements.

- Everything in Scale
- Custom data retention policies
- Advanced security controls and audit logging
- SSO and identity provider integration
- Custom SLAs
- Dedicated account management
- API access for integration with existing data infrastructure

### Managed (Simba Managed)

**Best for:** Organizations that want hands-off, expert-driven marketing mix modeling.

- Simba's team of **PhD statisticians** builds, validates, and maintains your models
- Full platform access plus expert model configuration and interpretation
- Regular reporting cadence tailored to your business
- Strategic consultation on media optimization
- Ideal for teams without in-house data science resources or those wanting a second expert opinion alongside their own analysis

---

## Workspace Configuration

A **workspace** is your dedicated environment in Simba. It contains your datasets, model configurations, results, and team members. Each workspace is isolated with its own encrypted storage.

### Setting up your workspace

After account creation, your default workspace is ready to use. To configure it:

1. Navigate to **Settings** from the main menu.
2. Under **Workspace Settings**, you can:
   - **Rename your workspace** to reflect your brand or project (e.g., "Acme Corp Q1 2026" or "Client: Greenfield Media").
   - **Set your default currency** for spend data display.
   - **Configure your date format** preference.
   - **Set your default KPI** if you consistently model the same target metric.

### Managing multiple workspaces (Scale, Enterprise, Managed)

On the Scale plan and above, you can create and manage multiple workspaces:

1. From the workspace switcher in the top navigation, click **Create New Workspace**.
2. Name the workspace and configure its settings independently.
3. Each workspace has **isolated data storage** — data uploaded to one workspace is never accessible from another. This is backed by separate AWS S3 buckets per workspace.
4. Switch between workspaces using the workspace dropdown.

This is particularly useful for agencies that need strict data separation between clients.

---

## Team Collaboration

### Inviting team members (Scale, Enterprise, Managed)

Team collaboration features are available on Scale, Enterprise, and Managed plans:

1. Go to **Settings > Team Management**.
2. Click **Invite Member**.
3. Enter the team member's email address.
4. Assign a role (see below).
5. The invited user will receive an email with a link to join your workspace.

### Roles and permissions

Simba uses role-based access control to manage what team members can do within a workspace:

| Role | Capabilities |
|---|---|
| **Owner** | Full control — manage billing, team, settings, and all modeling features |
| **Admin** | Manage team members, data, and models. Cannot modify billing. |
| **Analyst** | Upload data, configure and run models, create scenarios, run optimization. Cannot manage team or settings. |
| **Viewer** | View results, reports, and dashboards. Cannot modify data or models. |

Roles can be updated at any time by the workspace Owner or Admin.

### Sharing results

Within a workspace, all team members can view model results based on their role permissions. To share results with stakeholders outside the platform:

- Export charts and reports as PDF or image files from the results dashboard.
- Share scenario comparisons as downloadable reports.
- Enterprise plans support scheduled report delivery via email.

---

## Security and Data Protection

Your data security is a core design principle, not an afterthought:

- **AES-256 encryption** for all data at rest
- **TLS 1.3** for all data in transit
- **Isolated AWS S3 buckets** per workspace — your data is never co-mingled with other customers
- **GDPR compliance** — your data rights are fully respected
- **Cyber Essentials certification** — independently verified security practices

No user-level or personally identifiable data is required. Simba works with aggregated marketing data (channel spend, impressions, conversions), which significantly reduces privacy risk by design.

For full details, see [Security and Compliance](../platform/security-and-compliance.md).

---

## Upgrading, Downgrading, and Billing

### Upgrading your plan

1. Go to **Settings > Billing**.
2. Click **Change Plan**.
3. Select your new plan and confirm.
4. Your new features are available immediately. You will be charged the prorated difference for the current billing period.

### Downgrading

You can downgrade at any time. The downgrade takes effect at the end of your current billing period. If you are downgrading from a plan with multiple workspaces, you will need to select which workspace to retain.

### Billing details

- Plans are billed monthly or annually (annual billing includes a discount — see [getsimba.ai](https://getsimba.ai) for details).
- Manage payment methods and view invoices in **Settings > Billing**.
- For Enterprise and Managed plan billing, contact your account manager or email **support@simba-mmm.com**.

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Did not receive verification email | Check your spam folder. If not found, click "Resend verification" on the login page. |
| Cannot access workspace after invitation | Ensure you are logged in with the email address that received the invitation. |
| Trial expired before evaluation was complete | Contact **support@simba-mmm.com** to discuss an extension. |
| Need to transfer workspace ownership | Go to Settings > Team Management and assign the Owner role to another team member. |

---

## Next Steps

- [Quick Start Guide](quick-start-guide.md) — Build your first model
- [Platform Overview](platform-overview.md) — Learn the interface
- [Data Requirements](../data-preparation/data-requirements.md) — Prepare your data for upload
- [Security and Compliance](../platform/security-and-compliance.md) — Detailed security documentation

For any account-related questions, contact **support@simba-mmm.com**.
