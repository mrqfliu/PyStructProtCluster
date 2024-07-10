# PyStructProtCluster
﻿
## Overview
﻿
PyStructProtCluster is a Python-based tool designed for the structural analysis of proteins through 3D structure files in PDB format. It generates dendrograms that illustrate the structural relationships between proteins, providing insights into their functions and evolutionary connections.
﻿
## Key Features
﻿
- **PDB File Processing**: Analyzes protein structures in PDB format.
- **Dendrogram Generation**: Creates visual representations of structural relationships.
- **Parallel Computation**: Efficiently computes pairwise alignments in parallel.
- **Customizable Parallelism**: Adjust the number of parallel processes as needed.
- **Evolutionary and Functional Insights**: Supports studies in protein evolution and function prediction.
﻿
## Prerequisites
﻿
- Python (compatible versions)
- USalign: An open-source tool for protein structure alignment. [GitHub Repository](https://github.com/pylelab/USalign)
﻿
## Directory Structure
﻿
- `pdbs/`: Directory for storing the PDB files of proteins to be analyzed.
- `list_pdb{i}{n}.txt`: Intermediate files generated during the pairwise comparison process, auto-generated and can be deleted before use.
- `test/af_output/`: Directory containing the similarity matrices and related output/error files.
﻿
## Installation
﻿
Clone the repository and ensure all dependencies are installed:
﻿
```bash
git clone https://github.com/your_username/PyStructProtCluster.git
cd PyStructProtCluster
```
﻿
## Usage
﻿
1. Place your PDB files in the `pdbs/` directory.
2. Change the environment path in `get_align.sh` to your own.
3. Run the complete workflow with:
﻿
```bash
bash get_align.sh
```
﻿
This command will execute the full process from PDB files to the generation of the `tree.nwk` file.
﻿
Alternatively, you can run the steps individually for debugging or detailed analysis:
﻿
1. Generate pairwise comparison sublists: `PdbFileListGenerator.py`
2. Compute similarity matrix in parallel: `get_align2.sh` (Edit `parallel_count` to set parallel processes)
3. Stack alignment outputs: `get_align.py`
4. Generate similarity matrix and save to CSV: `similarity_matrix.py`
5. Output dendrogram file: `generate_tree.py`
﻿
## Scripts
﻿
- `PdbFileListGenerator.py`: Generates sublists for pairwise structure comparisons.
- `get_align2.sh`: Executes the pairwise alignment in parallel for performance.
- `get_align.py`: Combines individual alignment results into a single text file (`combined_similarity.txt`).
- `similarity_matrix.py`: Creates a similarity matrix from the alignment results.
- `generate_tree.py`: Produces a `tree.nwk` file for dendrogram visualization.
﻿
## Visualization
﻿
Visualize the `tree.nwk` file using the iTOL web tool for an interactive dendrogram. [iTOL Website](https://itol.embl.de/)

## License

PyStructProtCluster is open-source software released under the MIT License. The full text of the license can be found in the LICENSE file in the repository.

## Disclaimer

This software is provided "as is", without any warranty of any kind, express or implied. No guarantees are made regarding its fitness for any particular purpose or non-infringement of any intellectual property. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from, out of, or in connection with the software or its use.
﻿
## Contributing

Contributions to the PyStructProtCluster project are welcome! As the sole author to date, I am open to feedback, bug reports, and enhancements that can help improve the tool for the community. Here's how you can contribute:
- Bug Reports: If you find any issues or bugs, please submit an issue with detailed information.
- Feature Requests: If you have ideas for new features, feel free to open a new issue to discuss your ideas.
- Pull Requests: If you have developed a fix or a new feature, submit a pull request. Make sure to follow the project's coding standards and include tests when applicable.

## Support
For support, please contact the maintainer at mrqfliu@163.com.
