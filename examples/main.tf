module "ocean_loadbalancer_attachment" {
  source  = "stevenfeltner/aws-k8s-lb/ocean"
  spotinst_token = "Redacted"
  spotinst_account = "Redacted"
  ocean_id = "o-123456"
  loadbalancerarn = "arn:aws:elasticloadbalancing:us-west-2:123456789:targetgroup/exampleLB/123456789"
  debug = true
}
