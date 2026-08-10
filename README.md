# Terraform AWS

Production-style AWS infrastructure built with Terraform, focused on reliability, security, observability, and infrastructure automation.

## Overview

This project demonstrates a modular Terraform architecture for deploying a highly available AWS network foundation across multiple Availability Zones.

The current implementation includes:

- Multi-AZ VPC architecture
- Public and private subnets
- Internet Gateway
- NAT Gateway per Availability Zone
- Public and private route tables
- Reusable Terraform modules
- Environment-specific configuration
- Terraform validation in CI
- TFLint static analysis
- Trivy Infrastructure-as-Code security scanning

## Architecture

```text
                    Internet
                       |
                 Internet Gateway
                       |
          +------------+------------+
          |                         |
   Public Subnet AZ-A          Public Subnet AZ-B
          |                         |
      NAT Gateway               NAT Gateway
          |                         |
   Private Subnet AZ-A         Private Subnet AZ-B
          |                         |
        Workloads                  Workloads