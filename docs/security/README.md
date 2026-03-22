# Security Overview — How Simba Protects Your Data

Simba is built with enterprise-grade security at every layer. Your marketing data is encrypted, isolated, and protected by industry-leading standards. We adhere to strict UK Government security standards, built for global brands who demand data sovereignty.

## Security at a Glance

| Capability | Standard |
|------------|----------|
| **Encryption at rest** | AES-256 |
| **Encryption in transit** | TLS 1.3 |
| **Infrastructure** | Isolated AWS S3 buckets |
| **Certification** | Cyber Essentials (UK Government) |
| **Privacy regulation** | Fully GDPR compliant |
| **Data minimization** | Strict data minimization policies |
| **Logging** | Zero-retention logging |
| **Model isolation** | Proprietary models protected by strict isolation layers |

## Detailed Documentation

- **[Data Encryption](data-encryption.md)** — How your data is encrypted at rest and in transit
- **[Infrastructure](infrastructure.md)** — AWS architecture, isolation, and availability
- **[Compliance](compliance.md)** — GDPR, Data Protection Act, and Cyber Essentials certification
- **[Data Sovereignty](data-sovereignty.md)** — Data residency, international transfers, and Standard Contractual Clauses

## Reporting Security Issues

If you discover a security vulnerability, please report it responsibly via **security@simba-mmm.com**. See our [Security Policy](../../SECURITY.md) for full details.

---

*See also: [FAQ](../faq/README.md) | [Privacy Policy](https://getsimba.ai/privacy) | [Terms of Service](https://getsimba.ai/terms)*

## Two-Factor Authentication (2FA)

Simba supports **TOTP-based two-factor authentication** for an additional layer of account security.

### Setting Up 2FA

1. Navigate to **Settings > Security** (or **Profile > Security**).
2. Click **Enable Two-Factor Authentication**.
3. Scan the QR code with your authenticator app (Google Authenticator, Authy, 1Password, etc.).
4. Enter the 6-digit verification code from your authenticator app to confirm setup.
5. 2FA is now active on your account.

### Logging In with 2FA

When 2FA is enabled, after entering your email and password you will be prompted to enter the current 6-digit code from your authenticator app.

### Disabling 2FA

If you need to disable 2FA:

1. Go to **Settings > Security**.
2. Click **Disable Two-Factor Authentication**.
3. Confirm the action by entering your current 2FA code.

We recommend keeping 2FA enabled for maximum account security, especially for accounts with access to sensitive marketing data.
