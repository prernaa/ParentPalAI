import os

# For OpenAI and HF keys - not uploaded to Github
DATA_FOLDER = "../../ParentPalAI_Data"

# To output data 
SHARED_DATA_FOLDER = "../data_to_share"

# a dataset of 1182 samples 
data_fstr = "dpo_dataset"
INPUT_DATASET_FPATH = os.path.join(SHARED_DATA_FOLDER, f"{data_fstr}.jsonl")
INPUT_DATASET_INFERENCE_FPATH = os.path.join(SHARED_DATA_FOLDER, f"{data_fstr}_output.jsonl")
INPUT_DATASET_EVAL_FPATH = os.path.join(SHARED_DATA_FOLDER, f"{data_fstr}_gpt_as_judge_output.jsonl")
INPUT_DATASET_DPO_LABELS_FPATH = os.path.join(SHARED_DATA_FOLDER, f"{data_fstr}_dpo_labels.jsonl")

# UNSEEN TEST SET FILES
test_fstr = "dpo_dataset_test"
TEST_DATASET_FPATH = os.path.join(SHARED_DATA_FOLDER, f"{test_fstr}.jsonl")
TEST_DATASET_INFERENCE_FPATH = os.path.join(SHARED_DATA_FOLDER, f"{test_fstr}_output_base_dpo.jsonl")
TEST_DATASET_EVAL_FPATH = os.path.join(SHARED_DATA_FOLDER, f"{test_fstr}_gpt_as_judge_output.jsonl")

## small trial dataset I first used just to test the code
# INPUT_DATASET_1_FPATH = os.path.join(SHARED_DATA_FOLDER, "dpo_dataset_trial_small_sample.jsonl")
