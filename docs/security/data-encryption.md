# Data Encryption — AES-256 at Rest, TLS 1.3 in Transit

Simba uses bank-grade encryption to protect your marketing data at every stage — whether it's stored on our servers or being transmitted between your browser and our platform.

## Encryption at Rest

All data stored within Simba is encrypted using **AES-256** (Advanced Encryption Standard with 256-bit keys):

- AES-256 is the same encryption standard used by financial institutions and government agencies
- Every dataset, model configuration, and result is encrypted before being written to storage
- Encryption keys are managed through secure key management infrastructure
- Proprietary models are protected by strict isolation layers

## Encryption in Transit

All data transmitted between your browser and Simba is protected using **TLS 1.3** (Transport Layer Security):

- TLS 1.3 is the latest and most secure version of the TLS protocol
- All API calls, data uploads, and platform interactions are encrypted in transit
- Older, less secure protocol versions are not supported
- Perfect forward secrecy ensures that past communications remain secure even if keys are compromised

## What This Means for You

- Your marketing data **cannot be read** by anyone without proper authorization — not even infrastructure administrators
- Data **in motion** between your browser and Simba is fully encrypted and cannot be intercepted
- Your competitive marketing data and business intelligence remain **confidential**

→ **Next**: [Infrastructure](infrastructure.md) | [Compliance](compliance.md)

---

*See also: [Security Overview](README.md) | [Data Sovereignty](data-sovereignty.md)*
