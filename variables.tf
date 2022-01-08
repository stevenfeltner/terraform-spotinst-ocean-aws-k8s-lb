variable "spotinst_token" {
  type        = string
  description = "Spot Personal Access token"
}

variable "spotinst_account" {
  type        = string
  description = "Spot account ID"
}

variable "ocean_id" {
  type        = string
  description = "ID of the Ocean cluster"
}

variable "loadbalancerarn" {
  type        = string
  description = "ARN of the loadbalancer"
}