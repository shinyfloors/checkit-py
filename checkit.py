import os
import sys
import datetime
import logging, logging.config


#
# Specify the path to your Bagit installation.
# NOTE: do not include the bagit.py file; just the folder that contains it!
#
path_to_bagit = "/users/example/bagit-python"

#
# Specify the path to your directory of bags.
#
path_to_parent_directory = "/users/example/bags/"

#
# Specify the path to your directory where you'd like logs output.
# This will be created if it doesn't already exist.
#
path_to_log_directory = "/users/example/checkit-logs"




# Import the Library Of Congress Bagit library
sys.path.append(path_to_bagit)
import bagit



# Set up a logger, so that validation results are written to a log file
path_to_log_file = path_to_log_directory + "/" + datetime.datetime.now().strftime("%Y-%M-%d-%H%M%S") + ".txt"
logging.basicConfig(level=logging.INFO, filename=path_to_log_file, filemode='w', format='%(asctime)-15s %(message)s')
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})



# Starting from the 'parent' directory of bags, traverse all subdirectories,
# looking for a file called "bagit.txt".
#
# The presence of this file indicates the current directory is a 'bag'; so we
# add this directory to a list of all known bags.
print "Finding bags..."
bags = []
for root, dirs, files in os.walk(path_to_parent_directory):
    for file in files:
        if file == "bagit.txt":
            bags.append(root)


# Count the total number of bags and print out
total = len(bags)

print "Found", total, "bags. Validating..."
print ""
print "Total", "\t", "Valid", "\t", "Invalid"


# Prepare some counters; as we check the validity of each bag, we'll increment
# the value of the `valid` or `invalid` bags accordingly.
valid = 0
invalid = 0


# Loop over each of the bags we identified above
for bag_path in bags:
    bag = bagit.Bag(bag_path)
    
    # Try to validate the current bag
    try:
        bag.validate()

        # If the bag didn't fail validation, we'll log its success and
        # increment the counter of valid bags.
        logging.info("Valid: %s", bag_path)
        valid += 1

    except bagit.BagValidationError as e:
        # If the validation failed, we'll log this failure and increment the
        # counter of invalid bags.
        logging.error("INVALID: %s. FAILURE: %s", bag_path, e);
        invalid += 1

    # Print out the current values of the total, valid and invalid bags.
    # NOTE: \r will ensure we overwrite the last numbers printed.
    #       \t is the 'tab' character, for spacing.
    sys.stdout.write("\r %i\t %i\t %i" % (total, valid, invalid))
    sys.stdout.flush()

# After processing all bags, we can check the counters we incremented above to
# verify if all bags validated OK.
if invalid > 0:
    print "\r\nThere are", invalid, "bags in error! Check log for details:"
    print path_to_log_file
else:
    print "\r\nAll bags validated ok :)"
