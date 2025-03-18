import yaml
import argparse
import os

def update_image_tag(new_image):
    """Update the image tag for all containers in deployment.yaml (assumed to be in the same directory)."""
    file_path = "deployment.yaml"

    with open(file_path, "r") as file:
        deployment = yaml.safe_load(file)

    if "kind" in deployment and deployment["kind"] == "Deployment":
        containers = deployment["spec"]["template"]["spec"]["containers"]

        for container in containers:
            print(f"Updating image for container '{container['name']}' from {container['image']} to {new_image}")
            container["image"] = new_image  

        with open(file_path, "w") as file:
            yaml.dump(deployment, file, default_flow_style=False)

        # print(f" Successfully updated deployment.yaml with new image: {new_image}")
    else:
        print("The file deployment.yaml is not a valid Deployment YAML")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", required=True, help="New image tag (e.g., 'repo/image:v1.2.3')")

    args = parser.parse_args()
    update_image_tag(args.version)