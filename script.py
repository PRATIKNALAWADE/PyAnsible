import subprocess

def run_ansible_playbook(playbook_path, inventory_path):
    """
    Run an Ansible playbook using the subprocess module.
    
    :param playbook_path: Path to the Ansible playbook file.
    :param inventory_path: Path to the Ansible inventory file.
    :return: None
    """
    try:
        result = subprocess.run(
            ['ansible-playbook', '-i', inventory_path, playbook_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print('Ansible playbook executed successfully.')
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print('Ansible playbook execution failed.')
        print(e.stderr)

if __name__ == '__main__':
    # Paths to the playbook and inventory files
    playbook_path = 'playbooks/setup.yml'
    inventory_path = 'inventory/hosts'
    
    # Run the Ansible playbook
    run_ansible_playbook(playbook_path, inventory_path)
