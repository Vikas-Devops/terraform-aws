variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the development VPC"
}

variable "availability_zones" {
  type        = list(string)
  description = "Availability zones for the development environment"
}

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "Public subnet CIDR blocks"
}

variable "private_subnet_cidrs" {
  type        = list(string)
  description = "Private subnet CIDR blocks"
}