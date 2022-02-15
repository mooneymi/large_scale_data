## FASTQ Files Location

`/home/courses/BMI535/data/VariantCalling/fastq/`

## Exome Capture Target Location

`/home/courses/BMI535/data/VariantCalling/1000GenomesExomeCapture/`

## GATK4 Best Practices

https://github.com/gatk-workflows/gatk4-data-processing

## GATK Bundle

`/home/courses/BMI535/data/VariantCalling/GATKBundle`

## FastQC

- https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
- Download: https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip

**Note: For the commands below you should start in your home directory (cd ~) on state. Also, you'll need to swap in your username anywhere you see <username>.
```
## Create symbolic link to your course folder
ln -s /home/courses/BMI535/students/<username> ~/BMI535

## Create a symbolic link called ~/var_data to easily access the data
ln -s /home/courses/BMI535/data/VariantCalling/ ~/var_data

## Download FASTQC, unzip, and change permissions
wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip
unzip fastqc_v0.11.9.zip
chmod 711 FastQC

## Add my FastQC directory to the PATH variable
## You can add this to your .bash_profile
export PATH="$HOME/FastQC/:$PATH"

## Make an output directory
mkdir ~/qc_analyses

fastqc -o ~/qc_analyses ~/var_data/fastq/SRR702072_1.filt.fastq ~/var_data/fastq/SRR702072_2.filt.fastq
```

## BWA

Main page: http://bio-bwa.sourceforge.net/

```
## Move to your course folder 
## (output for steps below may be too large for your home directory)
cd /home/courses/BMI535/students/<username>

## Install BWA
conda install -c bioconda bwa
which bwa
```

```
## Run bwa index to create index on hg19 genome file
## *** You don't need to run this - it's already created ***
## *** Just included so you know that this is a step ***
bwa index ~/var_data/GATKBundle/ucsc.hg19.fasta
```

```
## Run bwa mem on our fastq file
bwa mem -Y -t 12 -R '@RG\tID:SRR702072\tPL:Illumina\tLB:SRR702072\tSM:SRR702072' ~/var_data/GATKBundle/ucsc.hg19.fasta ~/var_data/fastq/SRR702072_1.filt.fastq ~/var_data/fastq/SRR702072_2.filt.fastq -o SRR702072.sam
```

# Samtools

Install samtools via conda

```
## Install Samtools
conda install -c bioconda samtools
```

Run `samtools flagstat` on our `.sam` file:

```
samtools flagstat SRR702072.sam
```


# GATK

Download, unzip with `unzip`, and add to your `$PATH`

```
wget https://github.com/broadinstitute/gatk/releases/download/4.1.4.1/gatk-4.1.4.1.zip
```

```
## List all utilities
gatk --list

## Convert SAM to BAM file
gatk SamFormatConverter -I SRR702072.sam -O SRR702072.bam

## Sort BAM file using SortSam
gatk SortSam -I SRR702072.bam -O sortedSRR702072.bam -SO coordinate
```

Try running `gatk MarkDuplicates` on `sortedSRR702072.bam` by [reading the man page!](https://gatk.broadinstitute.org/hc/en-us/articles/360037052812-MarkDuplicates-Picard-)

```
gatk MarkDuplicates --help
```

## Where is GATK on exacloud?

```
/opt/installed/gatk-4.0.0.0/gatk
```

## Useful GATK Links

- GATK Command-line Syntax: https://gatk.broadinstitute.org/hc/en-us/articles/360035531892
- GATK Data Preprocessing for Variant Discovery (start here, thanks Mike!): https://gatk.broadinstitute.org/hc/en-us/articles/360035535912-Data-pre-processing-for-variant-discovery
- GATK Best Practices Tutorials: https://www.broadinstitute.org/partnerships/education/broade/best-practices-variant-calling-gatk-1
- HaplotypeCaller: https://docs.google.com/file/d/0B2dK2q40HDWeYzVTUGs0bjM3M1E/preview
