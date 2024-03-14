import hashlib

# Genesis block parameters from the provided C++ code
pszTimestamp = "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."
genesisOutputScript = "04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f"

def hash256(data):
  """Double SHA256 hash function"""
  sha = hashlib.sha256(data)
  return hashlib.sha256(sha.digest()).hexdigest()

def merkle_root(tx_hashes):
  """Calculates the Merkle Root for a list of transaction hashes"""
  if len(tx_hashes) == 0:
    # Special case for empty block (e.g., genesis block)
    return "0000000000000000000000000000000000000000000000000000000000000000"
  elif len(tx_hashes) == 1:
    return tx_hashes[0]
  else:
    # Recursive approach for building the Merkle tree
    mid = len(tx_hashes) // 2
    left_root = merkle_root(tx_hashes[:mid])
    right_root = merkle_root(tx_hashes[mid:])
    combined = left_root + right_root
    return hash256(combined.encode())

# Empty list for transactions (assuming genesis block)
tx_hashes = []

# Calculate Merkle Root
merkle_root_hash = merkle_root(tx_hashes)

# Print the Merkle Root hash
print(merkle_root_hash)
