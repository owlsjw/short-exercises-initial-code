"""
Short Exercises #3
"""
import test_helpers

small_candidates = test_helpers.read_CSV_file("tests/small_candidates.csv")

candidates = test_helpers.read_CSV_file("tests/candidates.csv")


def find_candidates_from_city(candidates, office_loc):
    """
    Given a list of candidates, construct a list of the candidate IDs
    for candidates with a campaign headquartered in the specified location.
    Inputs:
        candidates: list of candidates
        office_loc (string, string): a tuple of the form
            (city name, state abbreviation)
    Returns: list of candidate IDs (strings)
    """
    candidate_id = []
    city_name, state_abbr = office_loc
    for candidate in candidates:
        if state_abbr == candidate["State"] and city_name == candidate["City"]:
            ds = candidate("Candidate_ID")
    return candidate_id.append[ds]

def construct_dict_from_lists(keys, values):
    """
    Given a list of (key, index) pair and a list of values, construct a
    dictionary that maps each key to the value in the list of values at the
    specified index.
    Inputs:
        keys: a list of (key, index) pairs, where each key is a (unique)
            immutable value (string, int, etc.), and each index is an integer
        values: a list of values
    Returns: dictionary
    """

    


def construct_homestate_dict(candidates):
    """
    Construct a dictionary that maps a candidate ID to the candidate's
    home state.
    Inputs:
        candidates: list of candidates
    Returns: dictionary that maps candidate id (string) to a state
        abbreviation (string)
    """
    id_state = {}
    for candidate in candidates:
        id = candidate["Candidate_ID"]
        if candidate not in id_state:
            id_state = {}
    id_state[id] = id_state.get(id,0) + candidate["State"]
    return id_state

def find_successful_fund_raisers(cand_to_count, threshold):
    """
    Given a dictionary that maps candidate IDs to the number of donations
    received by the campaigns, compute a list of the candidates who have
    received at least the threshold number of contributions.
    Inputs:
        cand_to_count: dictionary that maps Candidate IDs to integers
        threshold (int): the threshold for labeling a candidate as successful
    Returns: list of Candidate IDs
    """




def construct_cands_by_state(candidates):
    """
    Construct a mapping from states to the candidates from that state.
    Inputs:
      candidates: list of candidate dictionaries
    Returns: dictionary that maps a state abbreviation (string) to a
     list of dictionaries for candidates from that state.
    """

    ### EXERCISE 5 -- Replace pass with your code
    pass
