module "ocean_loadbalancer_attachment" {
  source  = "stevenfeltner/ocean_loadbalancer_attachment/spotinst"
  spotinst_token = "Redacted"
  spotinst_account = "Redacted"
  ocean_id = "o-123456"
  loadbalancerarn = "arn:aws:elasticloadbalancing:us-west-2:303703646777:targetgroup/steven-codedeploy/ff0df4b188cf35cc"
}
