from aws_cdk import (
    # Duration,
    Stack, Duration, Tags
    # aws_sqs as sqs,
)
from aws_cdk.aws_ecr_assets import DockerImageAsset
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_ecr as ecr,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_certificatemanager as acm
)

class MyprojectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc.from_lookup(self, "",
                                  vpc_id="vpc-....")
        security_group = ec2.SecurityGroup(self,
                                           "",
                                           vpc=vpc,
                                           security_group_name="",
                                           allow_all_outbound=True,
                                           description="Security Group for ECS Deployment")
        security_group.add_ingress_rule(peer=ec2.Peer.any_ipv4(), connection=ec2.Port.tcp(8000),
                                        description="Django Inbound Rule")

        cluster = ecs.Cluster.from_cluster_attributes(self,
                                                      "",
                                                      cluster_name="", vpc=vpc,
                                                      security_groups=[security_group])
        loadbalancer_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "sakshammittal-fargate",
                                                                                  cluster=cluster,  # Required
                                                                                  cpu=256,  # Default is 256
                                                                                  desired_count=2,  # Default is 1
                                                                                  task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                                                      image=ecs.ContainerImage.from_docker_image_asset(
                                                                                          asset=DockerImageAsset(self,
                                                                                                                 id="myproject-image",
                                                                                                                 directory='../')
                                                                                      ),
                                                                                      container_port=8000,
                                                                                      container_name="myproject-container"
                                                                                  ),
                                                                                  memory_limit_mib=512,
                                                                                  max_healthy_percent=200,
                                                                                  min_healthy_percent=50,
                                                                                  # Default is 512
                                                                                  public_load_balancer=True,
                                                                                  certificate=acm.Certificate.from_certificate_arn(
                                                                                      self, "DomainCertificate",
                                                                                      certificate_arn="arn:aws:acm:region_name:account:certificate/...."
                                                                                  )
                                                                                  )
        scalable_target = loadbalancer_service.service.auto_scale_task_count(
            min_capacity=1,
            max_capacity=5
        )
        scalable_target.scale_on_cpu_utilization("CpuScaling",
                                                 target_utilization_percent=40
                                                 )

        scalable_target.scale_on_memory_utilization("MemoryScaling",
                                                    target_utilization_percent=40
                                                    )
        loadbalancer_service.target_group.configure_health_check(
            enabled=True,
            healthy_threshold_count=2,
            path='/',
            interval=Duration.seconds(20),
            timeout=Duration.seconds(10)
        )

        route53.ARecord(self, "AliasRecord",
                        record_name='',
                        zone=route53.HostedZone.from_lookup(
                            self,
                            "HostedZone",
                            domain_name="devfactory.com"
                        ),
                        ttl=Duration.minutes(1),
                        target=route53.RecordTarget.from_alias(
                            targets.LoadBalancerTarget(loadbalancer_service.load_balancer)),
                        )

        Tags.of(self).add("Owner", "Saksham Mittal")
        Tags.of(self).add("AD", "sakshammittal")
        Tags.of(self).add("Email", "saksham@trilogy.com")
        Tags.of(self).add("Quarter", "TU-22")
        Tags.of(self).add("Project", "MyProject")
