# Infrastructure — AWS Architecture and Data Isolation

Simba runs on secure AWS infrastructure designed for high availability, performance, and strict data isolation between customers.

## AWS Cloud Infrastructure

Simba is hosted on Amazon Web Services (AWS), the industry-leading cloud platform:

- **Compute**: Scalable infrastructure that handles model fitting, optimization, and scenario planning
- **Storage**: Data is stored in **isolated AWS S3 buckets** with per-customer separation
- **Availability**: High-availability architecture designed for enterprise uptime requirements
- **Regions**: Infrastructure designed for global brand requirements

## Data Isolation

Customer data isolation is a core architectural principle:

- **Per-customer S3 buckets** — Your data is stored in isolated storage, completely separate from other customers
- **Model isolation** — Proprietary models are protected by strict isolation layers
- **No cross-tenant access** — One customer's data is never accessible from another customer's context
- **Logical and physical separation** — Multiple layers of isolation at the application, network, and storage level

## Architecture Principles

- **Defense in depth** — Multiple layers of security controls
- **Least privilege** — Access is restricted to the minimum required for each component
- **Secure by default** — All new infrastructure components are hardened before deployment
- **Continuous monitoring** — Infrastructure is monitored for security events

→ **Next**: [Compliance](compliance.md) | [Data Encryption](data-encryption.md)

---

*See also: [Security Overview](README.md) | [Data Sovereignty](data-sovereignty.md)*
