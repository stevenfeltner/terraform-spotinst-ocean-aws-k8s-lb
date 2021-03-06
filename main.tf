# Call Spot API to add/remove loadbalancer
resource "null_resource" "ocean_loadbalancer_attachment" {
  triggers = {
    cmd = "${path.module}/scripts/spot-ocean-aws"
    loadbalancerarn = var.loadbalancerarn
    ocean_id = var.ocean_id
    account_id = var.spotinst_account
    token = var.spotinst_token
  }
  provisioner "local-exec" {
    interpreter = ["/bin/bash", "-c"]
    command = "${self.triggers.cmd} add ${self.triggers.loadbalancerarn} ${self.triggers.ocean_id} ${self.triggers.account_id} ${self.triggers.token}"
  }
  provisioner "local-exec" {
    when = destroy
    interpreter = ["/bin/bash", "-c"]
    command = "${self.triggers.cmd} delete ${self.triggers.loadbalancerarn} ${self.triggers.ocean_id} ${self.triggers.account_id} ${self.triggers.token}"
  }
}
