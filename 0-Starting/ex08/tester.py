from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# Testing my tqdm implementation
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# Testing the original tqdm implementation
# Install with: pip install tqdm
for elem in tqdm(range(333)):
    sleep(0.005)
print()
