# Ocean AWS K8s Loadbalancer Terraform Module

Terraform module to aid in attaching and detaching loadbalancers to an existing Ocean cluster.

## Usage

```hcl
module "ocean_loadbalancer_attachment" {
  source  = "stevenfeltner/aws-k8s-lb/ocean"
  spotinst_token = "Redacted"
  spotinst_account = "Redacted"
  ocean_id = "o-123456"
  loadbalancerarn = "arn:aws:elasticloadbalancing:us-west-2:123456789:targetgroup/exampleLB/123456789"
}
```

## Documentation

If you're new to [Spot](https://spot.io/) and want to get started, please checkout our [Getting Started](https://docs.spot.io/connect-your-cloud-provider/) guide, available on the [Spot Documentation](https://docs.spot.io/) website.

## Getting Help

We use GitHub issues for tracking bugs and feature requests. Please use these community resources for getting help:

- Ask a question on [Stack Overflow](https://stackoverflow.com/) and tag it with [terraform-spotinst](https://stackoverflow.com/questions/tagged/terraform-spotinst/).
- Join our [Spot](https://spot.io/) community on [Slack](http://slack.spot.io/).
- Open an issue.

## Community

- [Slack](http://slack.spot.io/)
- [Twitter](https://twitter.com/spot_hq/)

## Contributing

Please see the [contribution guidelines](.github/CONTRIBUTING.md).

## License

Code is licensed under the [Apache License 2.0](LICENSE).
