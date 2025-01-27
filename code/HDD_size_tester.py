import os

def fill_disk(target_size_in_gb, file_size_in_mb):
    # Convert the target size from GB to bytes
    target_size_in_bytes = target_size_in_gb * 1024 * 1024 * 1024
    total_written = 0
    file_count = 0
    
    # Loop until the disk is filled to the target size
    while total_written < target_size_in_bytes:
        # Create a dummy file of the specified size (file_size_in_mb)
        file_name = f"test_file_{file_count}.bin"
        
        with open(file_name, 'wb') as f:
            # Write 'file_size_in_mb' MB of data to the file
            f.write(b'\0' * file_size_in_mb * 1024 * 1024)
        
        total_written += file_size_in_mb * 1024 * 1024
        file_count += 1
        print(f"Written {total_written / (1024 * 1024 * 1024):.2f} GB...")
        
    print("Target size reached!")

# Example usage: Fill the disk with 500 GB of dummy data, in 1 GB chunks
fill_disk(500, 1000)
