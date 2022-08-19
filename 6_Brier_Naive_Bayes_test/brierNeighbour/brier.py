"""
Brier Score with Naive Bayes
"""

# IMPORTS
import numpy as np
import sys
from pathlib import Path 
file = Path(__file__).resolve()
sys.path.append(file.parents[1])






def vecteur_from_table_3d_proba_uni(aa_origine,
                                    aa_context,
                                    dict_2d,
                                    dict_3d,
                                    position,
                                    pseudo_counter_3D,
                                    alphabet):

    vect_distribution = []
    for aa in alphabet:
        vect_distribution.append(dict_2d[aa_origine][aa])
        
    if aa_context == "None":
        return vect_distribution
                

    else:
        table_3d = dict_3d[position][pseudo_counter_3D]
        vect = []
        for aa in alphabet:
            vect.append(table_3d[aa_origine][aa][aa_context])
        
        total_list_vect = [vect_distribution, vect]

        # COORDINATE WISE PRODUCT
        final_vector = np.prod(np.vstack(total_list_vect), axis=0)
        # print(f"FINAL VECTOR: {final_vector}")

        # VECTOR NORMALIZATION
        final_vector_normalized = final_vector/np.sum(final_vector)
        return final_vector_normalized
        



def vecteur_from_table_3d_proba_multi(aa_origine,
                                    list_aa_context,
                                    dict_2d,
                                    dict_3d,
                                    position,
                                    pseudo_counter_3D,
                                    alphabet):

    vect_distribution = []
    for aa in alphabet:
        vect_distribution.append(dict_2d[aa_origine][aa])
        
    if list_aa_context == []:
        return vect_distribution
                
    else:
        total_list_vect = [vect_distribution]
        for i in range(1, position+1):
            table_3d = dict_3d[i][pseudo_counter_3D]
            vect = []
            for aa in alphabet:
                vect.append(table_3d[aa_origine][aa][list_aa_context[i-1]])
            
            total_list_vect.append(vect)

        # COORDINATE WISE PRODUCT
        final_vector = np.prod(np.vstack(total_list_vect), axis=0)
        # print(f"FINAL VECTOR: {final_vector}")

        # VECTOR NORMALIZATION
        final_vector_normalized = final_vector/np.sum(final_vector)
        return final_vector_normalized




def vecteur_from_table_3d_proba_full(aa_origine,
                                    list_aa_context,
                                    dict_2d,
                                    dict_3d,
                                    position,
                                    pseudo_counter_3D,
                                    alphabet):

    vect_distribution = []
    for aa in alphabet:
        vect_distribution.append(dict_2d[aa_origine][aa])
        
    if list_aa_context == []:
        return vect_distribution
                
    else:
        total_list_vect = [vect_distribution]
        for i in range(1, position+1):
            j = 0
            for direction in ["ol", "or", "dl", "dr"]:
                table_3d = dict_3d[(direction,i)][pseudo_counter_3D]
                vect = []
                for aa in alphabet:
                    vect.append(table_3d[aa_origine][aa][list_aa_context[4*(i-1)+j]]) # cycle over the 4 directions
                j += 1
            
                total_list_vect.append(vect)

        # COORDINATE WISE PRODUCT
        final_vector = np.prod(np.vstack(total_list_vect), axis=0)
        # print(f"FINAL VECTOR: {final_vector}")

        # VECTOR NORMALIZATION
        final_vector_normalized = final_vector/np.sum(final_vector)
        return final_vector_normalized







def vecteur_from_table_3d_proba_semi_full(aa_origine,
                                    list_aa_context,
                                    dict_2d,
                                    dict_3d,
                                    position,
                                    pseudo_counter_3D,
                                    alphabet,
                                    direction_list):

    vect_distribution = []
    for aa in alphabet:
        vect_distribution.append(dict_2d[aa_origine][aa])
        
    if list_aa_context == []:
        return vect_distribution
                
    else:
        total_list_vect = [vect_distribution]
        for i in range(1, position+1):
            j = 0
            for direction in direction_list:
                table_3d = dict_3d[(direction,i)][pseudo_counter_3D]
                vect = []
                for aa in alphabet:
                    vect.append(table_3d[aa_origine][aa][list_aa_context[2*(i-1)+j]]) # cycle over the 2 directions
                j += 1
            
                total_list_vect.append(vect)

        # COORDINATE WISE PRODUCT
        final_vector = np.prod(np.vstack(total_list_vect), axis=0)
        # print(f"FINAL VECTOR: {final_vector}")

        # VECTOR NORMALIZATION
        final_vector_normalized = final_vector/np.sum(final_vector)
        return final_vector_normalized







def unit_brier_naive_bayes(vect, aa_destination, alphabet):
    """Compute the brier score for a vector of prediction
       and the correct prediction aa_destination

    Args:
        vect (list): probability of mutation in each element of alphabet
        aa_destination (str): correct prediction
        alphabet (list): list of characters of interest

    Returns:
        float: brier score
    """
    unit_brier = 0
    for index, aa in enumerate(alphabet):
        unit_brier += (vect[index] - int(aa_destination == aa))**2
    return unit_brier
