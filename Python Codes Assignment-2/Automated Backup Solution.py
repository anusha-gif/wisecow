import subprocess
import datetime

def backup_directory(source_dir, destination_host, destination_dir, ssh_key_path):
    # Generate timestamp for the backup
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Compose the rsync command
    rsync_command = [
        "rsync",
        "-avz",
        "-e", f"ssh -i {ssh_key_path}",
        "--delete",
        source_dir,
        f"{destination_host}:{destination_dir}/{timestamp}"
    ]

    try:
        # Execute the rsync command
        subprocess.run(rsync_command, check=True)
        print("Backup completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Backup failed: {e}")
        return False
    
    return True

def main():
    # Define backup parameters
    source_dir = "/path/to/source/directory"
    destination_host = "example@example.com"
    destination_dir = "/path/to/remote/backup/directory"
    ssh_key_path = "/path/to/ssh/key"

    # Perform the backup
    success = backup_directory(source_dir, destination_host, destination_dir, ssh_key_path)

    # Write backup status to a log file
    with open("backup_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {'Success' if success else 'Failure'}\n")

if __name__ == "__main__":
    main()
