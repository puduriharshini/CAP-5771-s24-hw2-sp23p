# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2780719051126377
    
    # Finding out the total number of variables:
    lung_cancer = 5
    no_lung_cancer = 5
    total_lung_cancer = lung_cancer + no_lung_cancer #we find out the total number of objects here
    entropy_lung_cancer = -(((lung_cancer/total_lung_cancer) * u.log2(lung_cancer/total_lung_cancer)) + ((no_lung_cancer/total_lung_cancer) * u.log2(no_lung_cancer/total_lung_cancer)))
    

    #Entropy for smoking at level 1:
    smoking_y_y = 4
    smoking_y_n = 1
    total_smoking_yes = smoking_y_y + smoking_y_n
    smoking_n_n = 4
    smoking_n_y = 1
    total_smoking_no = smoking_n_y+ smoking_n_n
    smoking_level1_entropy = -(((total_smoking_yes/total_lung_cancer) * (((smoking_y_y/total_smoking_yes) * u.log2(smoking_y_y/total_smoking_yes)) + ((smoking_y_n/total_smoking_yes) * u.log2(smoking_y_n/total_smoking_yes)))) + ((total_smoking_no/total_lung_cancer) * (((smoking_n_y/total_smoking_no) * u.log2(smoking_n_y/total_smoking_no)) + ((smoking_n_n/total_smoking_no) * u.log2(smoking_n_n/total_smoking_no)))))
    print("1(a) - Entropy for smoking at Level 1 is: " +str(smoking_level1_entropy))
    smoking_level1_info_gain = entropy_lung_cancer - smoking_level1_entropy
    print("1(a) - Information gain for smoking at level 1 is: " +str(smoking_level1_info_gain))

    level1["cough"] = -1.0
    level1["cough_info_gain"] = 0.034851554559677034

    #Entropy for cough at level 1:
    cough_y_y = 4
    cough_y_n = 3
    total_cough_yes = cough_y_y + cough_y_n
    cough_n_n = 2
    cough_n_y = 1
    total_cough_no = cough_n_y + cough_n_n
    cough_level1_entropy = -(((total_cough_yes/total_lung_cancer) * (((cough_y_y/total_cough_yes) * u.log2(cough_y_y/total_cough_yes)) + ((cough_y_n/total_cough_yes) * u.log2(cough_y_n/total_cough_yes)))) + ((total_cough_no/total_lung_cancer) * (((cough_n_y/total_cough_no) * u.log2(cough_n_y/total_cough_no)) + ((cough_n_n/total_cough_no) * u.log2(cough_n_n/total_cough_no)))))
    print("1(a) - Entropy for cough at level 1 is: " +str(cough_level1_entropy))
    cough_level1_info_gain = entropy_lung_cancer - cough_level1_entropy
    print("1(a) - Information gain for cough at level 1 is: " +str(cough_level1_info_gain))

    level1["radon"] = -1.0
    level1["radon_info_gain"] = 0.23645279766002802
    
    #Entropy for radon at level 1:
    radon_y_y = 2
    radon_y_n = 0
    total_radon_yes = radon_y_y + radon_y_n
    radon_n_y = 3
    radon_n_n = 5
    total_radon_no = radon_n_y + radon_n_n
    radon_level1_entropy = -(((total_radon_yes/total_lung_cancer) * (((radon_y_y/total_radon_yes) * u.log2(radon_y_y/total_radon_yes)) + ((radon_y_n/total_radon_yes) * 0 ))) + ((total_radon_no/total_lung_cancer) * (((radon_n_y/total_radon_no) * u.log2(radon_n_y/total_radon_no)) + ((radon_n_n/total_radon_no) * u.log2(radon_n_n/total_radon_no)))))
    print("1(a) - Entropy for radon at level 1 is: " +str(radon_level1_entropy))
    radon_level1_info_gain = entropy_lung_cancer - radon_level1_entropy
    print("1(a) - Information gain for radon at level 1 is: " +str(radon_level1_info_gain))


    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = 0.02904940554533142

    #Entropy for the weight loss at level 1:
    weight_y_y = 3
    weight_y_n = 2
    total_weight_yes = weight_y_y + weight_y_n
    weight_n_y = 2
    weight_n_n = 3
    weight_no_tot = weight_n_y + weight_n_n
    weight_level1_entropy = -(((total_weight_yes/total_lung_cancer) * (((weight_y_y/total_weight_yes) * u.log2(weight_y_y/total_weight_yes)) + ((weight_y_n/total_weight_yes) * u.log2(weight_y_n/total_weight_yes) ))) + ((weight_no_tot/total_lung_cancer) * (((weight_n_y/weight_no_tot) * u.log2(weight_n_y/weight_no_tot)) + ((weight_n_n/weight_no_tot) * u.log2(weight_n_n/weight_no_tot)))))
    print("1(a) - Entropy for weight loss at level 1 is: " +str(weight_level1_entropy))
    weight_level1_info_gain = entropy_lung_cancer - weight_level1_entropy
    print("1(a) - Information gain for weight loss at level 1 is: " +str(weight_level1_info_gain ))

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = -1.0
    
    #Entropy of the left system at level 2
    level2_left_y = 4
    level2_left_n = 1
    total_level2_left = level2_left_y + level2_left_n
    entropy_level2_left = -(((level2_left_y/total_level2_left) * u.log2(level2_left_y/total_level2_left)) + ((level2_left_n/total_level2_left) * u.log2(level2_left_n/total_level2_left)))
    
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = -1.0

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.07290559532005603
    
    #Level-2 radon left
    level2_radon_left_y_y = 1
    level2_radon_left_y_n = 0
    total_level2_radon_left_yes = level2_radon_left_y_y + level2_radon_left_y_n
    level2_radon_left_n_y = 3
    level2_radon_left_n_n = 1
    total_level2_radon_left_n = level2_radon_left_n_y + level2_radon_left_n_n
    radon_entropy_level2_left = -(((total_level2_radon_left_yes/total_level2_left) * (((level2_radon_left_y_y/total_level2_radon_left_yes) * u.log2(level2_radon_left_y_y/total_level2_radon_left_yes)) + ((level2_radon_left_y_n/total_level2_radon_left_yes) * 0))) + ((total_level2_radon_left_n/total_level2_left) * (((level2_radon_left_n_y/total_level2_radon_left_n) * u.log2(level2_radon_left_n_y/total_level2_radon_left_n)) + ((level2_radon_left_n_n/total_level2_radon_left_n) * u.log2(level2_radon_left_n_n/total_level2_radon_left_n)))))
    print("1(a) - Entropy for radon at level 2 left is: " +str(radon_entropy_level2_left))
    radon_level2_left_info_gain = entropy_level2_left - radon_entropy_level2_left
    print("1(a) - Information gain for radon at level 2 left is: " +str(radon_level2_left_info_gain))


    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.7219280948873623

    #Level-2 cough left:
    level2_cough_left_y_y = 4
    level2_cough_left_y_n = 0
    total_level2_cough_left_y = level2_cough_left_y_y + level2_cough_left_y_n
    level2_cough_left_n_y = 0
    level2_cough_left_n_n = 1
    total_level2_cough_left_n= level2_cough_left_n_y + level2_cough_left_n_n
    cough_level2_left_entropy= (((total_level2_cough_left_y/total_level2_left) * (((level2_cough_left_y_y/total_level2_cough_left_y) * u.log2(level2_cough_left_y_y/total_level2_cough_left_y)) + ((level2_cough_left_y_n/total_level2_cough_left_y) * 0))) + ((total_level2_cough_left_n/total_level2_left) * (((level2_cough_left_n_y/total_level2_cough_left_n) * 0) + ((level2_cough_left_n_n/total_level2_cough_left_n) * u.log2(level2_cough_left_n_n/total_level2_cough_left_n)))))
    print("1(a) - Entropy for cough at level 2 left is: " +str(cough_level2_left_entropy))
    cough_level2_left_info_gain = entropy_level2_left - cough_level2_left_entropy
    print("1(a) - Information gain for cough at level 2 left is: " +str(cough_level2_left_info_gain))
    
    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = 0.17095059445466865

    #Level-2 weight loss left:
    level2_weight_left_y_y = 2
    level2_weight_left_y_n = 0
    total_level2_weight_left_y = level2_weight_left_y_y + level2_weight_left_y_n
    level2_weight_left_n_y = 2
    level2_weight_left_n_n = 1
    total_level2_weight_left_n = level2_weight_left_n_y + level2_weight_left_n_n
    weight_level2_left_entropy = -(((total_level2_weight_left_y/total_level2_left) * (((level2_weight_left_y_y/total_level2_weight_left_y) * u.log2(level2_weight_left_y_y/total_level2_weight_left_y)) + ((level2_weight_left_y_n/total_level2_weight_left_y) * 0))) + ((total_level2_weight_left_n/total_level2_left) * (((level2_weight_left_n_y/total_level2_weight_left_n) * (u.log2(level2_weight_left_n_y/total_level2_weight_left_n))) + ((level2_weight_left_n_n/total_level2_weight_left_n) * u.log2(level2_weight_left_n_n/total_level2_weight_left_n)))))
    print("1(a) - Entropy for weight loss at level 2 left is: " +str(weight_level2_left_entropy))
    weight_level2_left_info_gain = entropy_level2_left - weight_level2_left_entropy
    print("1(a) - Information gain for weight loss at level 2 left is: " +str(weight_level2_left_info_gain))

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219280948873623

    #Level-2 right entropy:
    level2_right_y = 1
    level2_right_n = 4
    total_level2_right= level2_right_y + level2_right_n
    entropy_l2_r = -(((level2_right_y/total_level2_right) * u.log2(level2_right_y/total_level2_right)) + ((level2_right_n/total_level2_right) * u.log2(level2_right_n/total_level2_right)))

    #Level-2 radon right:
    level2_radon_right_y_y = 1
    level2_radon_right_y_n = 0
    total_level2_radon_right_y = level2_radon_right_y_y + level2_radon_right_y_n
    level2_radon_right_n_y = 0
    level2_radon_right_n_n = 4
    total_level2_radon_right_n = level2_radon_right_n_y + level2_radon_right_n_n
    radon_level2_right_entropy = (((total_level2_radon_right_y/total_level2_right) * (((level2_radon_right_y_y/total_level2_radon_right_y) * u.log2(level2_radon_right_y_y/total_level2_radon_right_y)) + ((level2_radon_right_y_n/total_level2_radon_right_y) * 0))) + ((total_level2_radon_right_n/total_level2_right) * (((level2_radon_right_n_y/total_level2_radon_right_n) * 0) + ((level2_radon_right_n_n/total_level2_radon_right_n) * u.log2(level2_radon_right_n_n/total_level2_radon_right_n)))))
    print("1(a) - Entropy for radon at level 2 right is: " +str(radon_level2_right_entropy))
    radon_level2_right_info_gain = entropy_l2_r - radon_level2_right_entropy
    print("1(a) - Information gain for radon at level 2 right is: " +str(radon_level2_right_info_gain))

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = 0.3219280948873623

    #Level-2 cough right:
    level2_cough_right_y_y = 0
    level2_cough_right_y_n = 3
    total_level2_cough_right_y = level2_cough_right_y_y + level2_cough_right_y_n
    level2_cough_right_n_y = 1
    level2_cough_right_n_n = 1
    total_level2_cough_right_n = level2_cough_right_n_y + level2_cough_right_n_n
    cough_level2_right_entropy = -(((total_level2_cough_right_y/total_level2_right) * (((level2_cough_right_y_y/total_level2_cough_right_y) * 0) + ((level2_cough_right_y_n/total_level2_cough_right_y) * (u.log2(level2_cough_right_y_n/total_level2_cough_right_y))))) + ((total_level2_cough_right_n/total_level2_right) * (((level2_cough_right_n_y/total_level2_cough_right_n) * (u.log2(level2_cough_right_n_y/total_level2_cough_right_n))) + ((level2_cough_right_n_n/total_level2_cough_right_n) * u.log2(level2_cough_right_n_n/total_level2_cough_right_n)))))
    print("1(a) - Entropy for cough at level 2 right is: " +str(cough_level2_right_entropy))
    cough_level2_right_info_gain = entropy_l2_r - cough_level2_right_entropy
    print("1(a) - Information gain for cough at level 2 right is: " +str(cough_level2_right_info_gain))

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = 0.17095059445466865

    #Level-2 weight loss right:
    level2_weight_right_y_y = 1
    level2_weight_right_y_n = 2
    total_level2_weight_right_y = level2_weight_right_y_y + level2_weight_right_y_n
    level2_weight_right_n_y = 0
    level2_weight_right_n_n = 2
    total_level2_weight_right_n = level2_weight_right_n_y + level2_weight_right_n_n
    weight_level2_right_entropy = -(((total_level2_weight_right_y/total_level2_right) * (((level2_weight_right_y_y/total_level2_weight_right_y) * u.log2(level2_weight_right_y_y/total_level2_weight_right_y)) + ((level2_weight_right_y_n/total_level2_weight_right_y) * (u.log2(level2_weight_right_y_n/total_level2_weight_right_y))))) + ((total_level2_weight_right_n/total_level2_right) * (((level2_weight_right_n_y/total_level2_weight_right_n) * 0) + ((level2_weight_right_n_n/total_level2_weight_right_n) * u.log2(level2_weight_right_n_n/total_level2_weight_right_n)))))
    print("1(a) - Entropy for weight loss at level 2 right is: " +str(weight_level2_right_entropy))
    weight_level2_right_info_gain = entropy_l2_r - weight_level2_right_entropy
    print("1(a) - Information gain for weight loss at level 2 right is: " +str(weight_level2_right_info_gain))

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right


    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("root")  # MUST STILL CREATE THE TREE *****
    smoking_y_l = tree.insert_left("Cough") #left split from the root is smoking "YES"
    smoking_n_r = tree.insert_right("Radon")
    smoking_y_l.insert_left("Yes")
    smoking_y_l.insert_right("No")
    smoking_n_r.insert_left("Yes")
    smoking_n_r.insert_right("No")
    
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    misplaced_items = 0
    total_items = 10
    training_error = (misplaced_items/total_items) * 100
    print("1Ans: The training error is: " +str(training_error))
    answer["training_error"] = 0.0  

    return answer



# ----------------------------------------------------------------------


def question2():
    answer = {}
    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.4253642047367425

    # entropy of the whole 
    d1 = ((0.3 * 0.3) + (0.8 * 0.4)) 
    d2 = ((0.7 * 0.6) + (0.2 * 0.2)) 
    d3 = ((0.2 * 0.2) + (0.3 * 0.3)) 
    d4 = d1 + d2 + d3
    d5 = -(((d1) * u.log2(d1)) + ((d2) * u.log2(d2)) + ((d3) * u.log2(d3)))
    print("(2a) - Entropy for the overall data is: " + str(d5))


    # Infogain
    answer["(b) x < 0.2"] = 0.17739286055515824
    #2-b x < = 0.2
    d6 = 0
    d7 = ((0.2 * 0.6) + (0.2 * 0.2))
    d8 = (0.2 * 0.2)
    d9 = ((0.8 * 0.4) + (0.3 * 0.3))
    d10 = (0.5 * 0.6)
    d11 = (0.3 * 0.3)
    d12 = d6 + d7 + d8
    d13 = d9 + d10 + d11
    d14 = d12 + d13
    d15 = -(((d7/d12) * (u.log2(d7/d12))) + ((d8/d12) * (u.log2(d8/d12))))
    d16 = -(((d9/d13) * (u.log2(d9/d13))) + ((d10/d13) * (u.log2(d10/d13))) + ((d11/d13) * (u.log2(d11/d13))))
    d17 = ((d12/d14) * d15) + ((d13/d14) * d16) 
    d18 = d5 - d17
    print("(2b) - Information gain for split x<= 0.2 is: " + str(d18))

    answer["(b) x < 0.7"] = 0.3557029418697566
    #2-b x < = 0.7
    d19 = (0.5 * 0.4)
    d20 = ((0.7 * 0.6) + (0.2 * 0.2))
    d21 = (0.2 * 0.2)
    d22 = ((0.3 * 0.4) + (0.3 * 0.3))
    d23 = 0
    d24 = (0.3 * 0.3)
    d25 = d19 + d20 + d21
    d26 = d22 + d23 + d24
    d27 = d25 + d26
    d28 = -(((d19/d25) * (u.log2(d19/d25))) + ((d20/d25) * (u.log2(d20/d25))) + ((d21/d25) * (u.log2(d21/d25))))
    d29 = -(((d22/d26) * (u.log2(d22/d26))) + ((d24/d26) * (u.log2(d24/d26))))
    d30 = ((d25/d27) * d28) + ((d26/d27) * d29) 
    d31 = d5 - d30
    print("(2b) - Information gain for split x<= 0.7 is: " + str(d31))

    answer["(b) y < 0.6"] = 0.34781842724338197
    #2-b y < = 0.6
    d32 = (0.3 * 0.3)
    d33 = (0.7 * 0.6) 
    d34 = (0.3 * 0.3)
    d35 = (0.8 * 0.4)
    d36 = (0.2 * 0.2)
    d37 = (0.2 * 0.2)
    d38 = d32 + d33 + d34
    d39 = d35 + d36 + d37
    d40 = d38 + d39
    d41 = -(((d32/d38) * (u.log2(d32/d38))) + ((d33/d38) * (u.log2(d33/d38))) + ((d34/d38) * (u.log2(d34/d38))))
    d42 = -(((d35/d39) * (u.log2(d35/d39))) + ((d36/d39) * (u.log2(d36/d39))) + ((d37/d39) * (u.log2(d37/d39))))
    d43 = ((d38/d40) * d41) + ((d39/d40) * d42) 
    d44 = d5 - d43
    print("(2b) - Information gain for split y<= 0.6 is: " + str(d44))

    # choose one of 'x=0.2', 'x=0.7', or 'y=0.6'
    answer["(c) attribute"] = "x=0.7"  

    #2-b entropy at left after split x = 0.7

    #2-b x < = 0.2 at level 2 left
    d45 = 0
    d46 = (0.2 * 0.2) + (0.2 * 0.6) 
    d47 = (0.2 * 0.2)
    d48 = d45 + d46 + d47
    d49 = (0.5 * 0.4)
    d50 = (0.5 * 0.6)
    d51 = 0
    d52 = d49 + d50 + d51
    d53 = d48 + d52
    d54 = -(((d45/d48) * 0) + ((d46/d48) * (u.log2(d46/d48))) + ((d47/d48) * (u.log2(d47/d48))))
    d55 = -(((d49/d52) * (u.log2(d49/d52))) + ((d50/d52) * (u.log2(d50/d52))) + ((d51/d52) * 0))
    d56 = ((d48/d53) * d54) + ((d52/d53) * d55) 
    d57 = (d30 - d56)
    print("(2b) - Information gain for split x<= 0.2 at level 2 left is: " + str(d57))

    #2-b y < = 0.6 at level 2 left
    d58 = 0
    d59 = (0.7 * 0.6) 
    d60 = 0
    d61 = d58 + d59 + d60
    d62 = (0.5 * 0.4)
    d63 = 0.04
    d64 = 0.04
    d65 = d62 + d63 + d64
    d66 = d61 + d65
    d67 = -(((d58/d61) * 0) + ((d59/d61) * (u.log2(d59/d61))) + ((d60/d61) * 0))
    d68 = -(((d62/d65) * (u.log2(d62/d65))) + ((d63/d65) * (u.log2(d63/d65))) + ((d64/d65) * (u.log2(d64/d65))))
    d69 = ((d61/d66) * d67) + ((d65/d66) * d68) 
    d70 = (d30 - d69)
    print("(2b) - Information gain for split y<= 0.6 at level 2 left is: " + str(d70))

    #2-b y < = 0.3 at level 2 left
    d71 = 0
    d72 = (0.3 * 0.7) 
    d73 = 0
    d74 = d71 + d72 + d73
    d75 = (0.5 * 0.4)
    d76 = (0.04 + (0.7 * 0.3))
    d77 = 0.04
    d78 = d75 + d76 + d77
    d79 = d74 + d78
    d80 = -(((d71/d74) * 0) + ((d72/d74) * (u.log2(d72/d74))) + ((d73/d74) * 0))
    d81 = -(((d75/d78) * (u.log2(d75/d78))) + ((d76/d78) * (u.log2(d76/d78))) + ((d77/d78) * (u.log2(d77/d78))))
    d82 = ((d74/d66) * d80) + ((d78/d79) * d81) 
    d83 = (d30 - d82)
    print("(2b) - Information gain for split y<= 0.3 at level 2 left is: " + str(d83))   

    #2-b y < = 0.8 at level 2 left
    d84 = (0.5 * 0.2)
    d85 = (0.6 * 0.7) 
    d86 = (0.2 * 0.2)
    d87 = d84 + d85 + d86
    d88 = (0.5 * 0.2)
    d89 = (0.2 * 0.2)
    d90 = 0
    d91 = d88 + d89 + d90
    d92 = d87 + d91
    d93 = -(((d84/d87) * (u.log2(d84/d87))) + ((d85/d87) * (u.log2(d85/d87))) + ((d86/d87) * (u.log2(d86/d87))))
    d94 = -(((d88/d91) * (u.log2(d88/d91))) + ((d89/d91) * (u.log2(d89/d91))) + ((d90/d91) * 0))
    d95 = ((d87/d92) * d93) + ((d91/d92) * d94) 
    d96 = (d30 - d95)
    print("(2b) - Information gain for split y<= 0.8 at level 2 left is: " + str(d96)) 

    #2-b x < =  0.2, y > 0.6 right level 3
    f1 = 0
    f2 = 0.04 
    f3 = 0.04
    f4 = f1 + f2 + f3
    f5 = (0.5 * 0.4)
    f6 = 0
    f7 = 0
    f8 = f5 + f6 + f7
    f9 = f4 + f8
    f10 = -(((f1/f4) * 0) + ((f2/f4) * (u.log2(f2/f4))) + ((f3/f4) * (u.log2(f3/f4))))
    f11 = -(((f5/f8) * (u.log2(f5/f8))) + ((f6/f8) * 0) + ((f7/f8) * 0))
    f12 = ((f4/f9) * f10) + ((f8/f9) * f11) 
    f13 = (d69 - f12)
    print("(2b) - Information gain for split x<= 0.2 at level 3 right is: " + str(f13))

    #2-b y < =  0.8, y > 0.6 right level 3
    f14 = (0.5 * 0.2)
    f15 = 0
    f16 = 0.04
    f17 = f14 + f15 + f16
    f18 = (0.5 * 0.2)
    f19 = 0.04
    f20 = 0
    f21 = f18 + f19 + f20
    f22 = f17 + f21
    f23 = -(((f14/f17) * (u.log2(f14/f17))) + ((f15/f17) * 0) + ((f16/f17) * (u.log2(f16/f17))))
    f24 = -(((f18/f21) * (u.log2(f18/f21))) + ((f19/f21) * (u.log2(f18/f21))) + ((f20/f21) * 0))
    f25 = ((f17/d66) * f23) + ((f21/f22) * f24) 
    f26 = (d69 - f25)
    print("(2b) - Information gain for split y<= 0.8 at level 3 right is: " + str(f26))

    #2-b y<0.6 at level 2 right
    f27 = 0.09
    f28 = 0 
    f29 = 0.09
    f30 = f27 + f28 + f29
    f31 = (0.4 * 0.3)
    f32 = 0
    f33 = 0
    f34 = f31 + f32 + f33
    f35 = f30 + f34
    f36 = -(((f27/f30) * (u.log2(f27/f30))) + ((f28/f30) * 0) + ((f29/f30) * (u.log2(f29/f30))))
    f37 = -(((f31/f34) * (u.log2(f31/f34))) + ((f32/f34) * 0) + ((f33/f34) * 0))
    f38 = ((f30/f35) * f36) + ((f34/f35) * f37) 
    f39 = (d30 - f38)
    print("(2b) - Information gain for split y<= 0.6 at level 2 right is: " + str(f39)) 

    #2-b y<0.3 at level 2 right
    f40 = 0.09
    f41 = 0 
    f42 = 0
    f43 = f40 + f41 + f42
    f44 = (0.4 * 0.3)
    f45 = 0
    f46 = 0.09
    f47 = f44 + f45 + f46
    f48 = f43 + f47
    f49 = -(((f40/f43) * (u.log2(f40/f43))) + ((f41/f43) * 0) + ((f42/f43) * 0))
    f50 = -(((f44/f47) * (u.log2(f44/f47))) + ((f45/f47) * 0) + ((f46/f47) * (u.log2(f46/f47))))
    f51 = ((f43/f48) * f49) + ((f47/f48) * f50) 
    f52 = (d30 - f51)
    print("(2b) - Information gain for split y<= 0.3 at level 2 right is: " + str(f52)) 

    #2-b y<0.8 at level 2 right
    f53 = (0.09 + (0.2 * 0.3))
    f54 = 0 
    f55 = 0.09
    f56 = f53 + f54 + f55
    f57 = 0.06
    f58 = 0
    f59 = 0
    f60 = f57 + f58 + f59
    f61 = f56 + f60
    f62 = -(((f53/f56) * (u.log2(f53/f56))) + ((f54/f56) * 0) + ((f55/f56) * (u.log2(f55/f56))))
    f63 = -(((f57/f60) * (u.log2(f57/f60))) + ((f58/f60) * 0) + ((f59/f60) * 0))
    f64 = ((f56/f61) * f62) + ((f60/f61) * f63) 
    f65 = (d30 - f64)
    print("(2b) - Information gain for split y<= 0.8 at level 2 right is: " + str(f65)) 

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("x <= 0.7")
    A = tree.insert_left("y <= 0.6")
    B = tree.insert_right("y <= 0.6")
    C = A.insert_right ("x <= 0.2")
    D = C.insert_left("y <= 0.8")
    E = B.insert_left("y <= 0.3")
    A.insert_left("B")
    C.insert_right("A")
    D.insert_left("C")
    D.insert_right("B")
    B.insert_right("A")
    E.insert_left("A")
    E.insert_right("C")
    
    answer["(d) full decision tree"] = tree
    return answer

# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5
    #The overall gini is:
    c0 = 10
    c1 = 10
    total_class = c0 + c1
    total_class_gini = (1 - (((c0/total_class)**2) + ((c1/total_class)**2)))
    print("3(a) - Gini for overall collection is: " + str(total_class_gini))

    # float
    answer["(b) Gini, ID"] = 0.0
    #Given that every customer ID is unique, Gini will be zero.

    answer["(c) Gini, Gender"] = 0.48
    #Gini for gender:
    c0_males = 6 #number of males in c0
    c0_females = 4 #number of females in c0
    c1_males = 4 #number of males in c1
    c1_females = 6 #number of females in c1
    total_males = c0_males + c1_males
    total_females = c0_females + c1_females
    gini_males = (1 - (((c0_males/total_males)**2) + ((c1_males/total_males)**2)))
    gini_females = (1 - (((c0_females/total_females)**2) + ((c1_females/total_females)**2)))
    total_gender = total_males + total_females
    gini_gender = ((total_males/total_gender) * gini_males) + ((total_females/total_gender) * gini_females)
    print("3(c) - Gini for gender is: " + str(gini_gender))

    answer["(d) Gini, Car type"] = 0.16250000000000003
    #Gini for car type:
    c0_family = 1
    c1_family = 3
    total_family = c0_family + c1_family
    c0_sports = 8
    c1_sports = 0
    total_sports = c0_sports + c1_sports
    no_luxury_c0 = 1
    no_luxury_c1 = 7
    total_luxury = no_luxury_c0 + no_luxury_c1
    gini_family = (1 - (((c0_family/total_family)**2) + ((c1_family/total_family)**2)))
    gini_sports = (1 - (((c0_sports/total_sports)**2) + ((c1_sports/total_sports)**2)))
    gini_luxury = (1 - (((no_luxury_c0/total_luxury)**2) + ((no_luxury_c1/total_luxury)**2)))
    total_car = total_family + total_sports + total_luxury
    gini_cartype = ((total_family/total_car) * gini_family) + ((total_sports/total_car) * gini_sports) + ((total_luxury/total_car) * gini_luxury)
    print("3(d) - Gini for car type is: " + str(gini_cartype))

    answer["(e) Gini, Shirt type"] = 0.49142857142857144
    # calulating gini for shirt type
    c0_small = 3
    c1_small = 2
    total_small = c0_small + c1_small
    c0_medium = 3
    c1_medium = 4
    total_medium = c0_medium + c1_medium
    c0_large = 2
    c1_large = 2
    total_large = c0_large + c1_large
    c0_extralarge = 2 
    c1_extralarge = 2
    total_extralarge = c0_extralarge + c1_extralarge
    gini_small = (1 - (((c0_small/total_small)**2) + ((c1_small/total_small)**2)))
    gini_medium = (1 - (((c0_medium/total_medium)**2) + ((c1_medium/total_medium)**2)))
    gini_large = (1 - (((c0_large/total_large)**2) + ((c1_large/total_large)**2)))
    gini_extralarge = (1 - (((c0_extralarge/total_extralarge)**2) + ((c1_extralarge/total_extralarge)**2)))
    total_shirt = total_small + total_medium + total_large + total_extralarge
    gini_shirt = ((total_small/total_shirt) * gini_small) + ((total_medium/total_shirt) * gini_medium) + ((total_large/total_shirt) * gini_large) + ((total_extralarge/total_shirt) * gini_extralarge)
    print("3(e) - Gini for shirt size is: " + str(gini_shirt))

    answer["(f) attr for splitting"] = "Car Type"

    # Explanatory text string
    answer["(f) explain choice"] = "In comparison to shirt size and gender, car type has the lowest Gini index, making it the best attribute. Since it results in overfitting, the split with ID shouldn't even be taken into consideration"

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ["binary, quantitative, nominal"]

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Time is considered binary because it has only two possible values (AM or PM) and it has no natural order, so it is ordinal"

    answer["b"] = ["continuous, quantitative, ratio"]
    answer["b: explain"] = "Brightness can take any value, and as long as it has true zero point it can be considered as a ratio, otherwise it is an interval"

    answer["c"] = ["discrete, qualitative, ordinal"]
    answer["c: explain"] = "People's judgments can be ranked, and these judgements cannot be continous"

    answer["d"] = ["continuous, quantitative, ratio"]
    answer["d: explain"] = "Angles can be of any values for example: 55.3 degrees and zero degrees means there is no angle, so it is ratio"

    answer["e"] = ["discrete, qualitative, ordinal"]
    answer["e: explain"] = "Medals have a natural order, so they are ordinal."

    answer["f"] = ["continuous, quantitative, ratio"]
    answer["f: explain"] = "Height can take any values and it has a true zero point"

    answer["g"] = ["discrete, quantitative, ratio"]
    answer["g: explain"] = "Number of patients in a hospital are finite and zero indicates no patients"

    answer["h"] = ["discrete, qualitative, nominal"]
    answer["h: explain"] = "ISBN numbers are unique and don't signify anything"

    answer["i"] = ["discrete, qualitative, ordinal"]
    answer["i: explain"] = "The degree of light passage has a natural order and they don't quantify how much light is passed"

    answer["j"] = ["discrete, qualitative, ordinal"]
    answer["j: explain"] = "Military ranks have a hierarchy"

    answer["k"] = ["continuous, quantitative, ratio"]
    answer["k: explain"] = "Distances can in measured in minuscule increments and have a true zero point"

    answer["l"] = ["continuous, quantitative, ratio"]
    answer["l: explain"] = "Density can take any value and zero densty means that object has no mass in a given volume"

    answer["m"] = ["discrete, qualitative, nominal"]
    answer["m: explain"] = "Coat check numbers don't signify anything"


    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Despite having greater accuracy in the testing and training sets (0.98 and 0.72, respectively), there is a significant discrepancy in accuracy between these two sets. which suggests that overfitting may have occurred. However, between the training and testing datasets, Model 2's accuracy barely decreased. Thus, for unseen instances, Model 2 is better"

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Model 2 is selected because Model 1's performance on unseen data is demonstrated in the table. This may be due to the model capturing noise or other factors (overfitting can also exist). However, compared to Model 1, the accuracy difference of Model 2 is much smaller"

    explain["c similarity"] = "Avoid Overfitting"
    explain["c similarity explain"] = "To lessen overfitting in a decision tree, both MDL and a pessimistic error estimate are employed"

    explain["c difference"] = "Implementation"
    explain["c difference explain"] = "MDL chooses the least complex model by following Ocam's razor principle. In contrast, a pessimistic error estimate adds a penalty that rises as more splits or leaves occur"

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # let's first find out the areas of each class
    area_6a = (0.3*0.2) + (0.6*0.5) + 0.4
    area_6b = (0.6*0.5) - (0.3*0.2)
    total_area = area_6a + area_6b

    #Gini before split
    gini_before_split = 1 - ((area_6a**2) + (area_6b**2))
    

    #Potential splits can be done at x = 0.5, x = 0.2, y = 0.4, y = 0.7

    #Gini at x1 = 0.5 level 1:
    split_less_x1_ar = 0.5     #ar = area
    split_gre_x1_ar = 0.5
    x1_less_a_area = (0.5 * 0.4) + (0.2 * 0.3)
    x1_less_b_area = (0.5 * 0.6) - (0.2 * 0.3)
    x1_less_area = x1_less_a_area + x1_less_b_area
    x1_greater_a_area = 0.5
    x1_greater_b_area = 0
    x1_greater_area = x1_greater_a_area + x1_greater_b_area
    x1_less_gini = (1 - (((x1_less_a_area/x1_less_area) **2) + ((x1_less_b_area/x1_less_area)**2)))
    x1_greater_gini = (1 - (((x1_greater_a_area/x1_greater_area)**2) + ((x1_greater_b_area/x1_greater_area)**2)))
    x1_gini = ((split_less_x1_ar) * (x1_less_gini)) + ((split_gre_x1_ar) * (x1_greater_gini))
    gini_x1_gain = gini_before_split - x1_gini
    print("6 - Gini for split at x <= 0.5 at level 1 is: "+str(x1_gini))
    print("6 - Gain for split at x <= 0.5 at level 1 is: "+str(gini_x1_gain))

    #Gini at x2 = 0.2 level 1:
    split_less_x2_ar = 0.2
    split_gre_x2_ar = 0.8
    x2_less_a_area = (0.2 * 0.4) + (0.2 * 0.3)
    x2_less_b_area = (0.2 * 0.3)
    x1_less_area = x2_less_a_area + x2_less_b_area
    x2_greater_a_area = (0.3 * 0.4) + (0.5 * 1.0)
    x2_greater_b_area = (0.3 * 0.6)
    x2_greater_area = x2_greater_a_area + x2_greater_b_area
    x2_less_gini = (1 - (((x2_less_a_area/x1_less_area) **2) + ((x2_less_b_area/x1_less_area)**2)))
    x2_greater_gini = (1 - (((x2_greater_a_area/x2_greater_area)**2) + ((x2_greater_b_area/x2_greater_area)**2)))
    x2_gini = ((split_less_x2_ar) * (x2_less_gini)) + ((split_gre_x2_ar) * (x2_greater_gini))
    gini_x2_gain = gini_before_split - x2_gini
    print("6 - Gini for split at x <= 0.2 at level 1 is: "+str(x2_gini))
    print("6 - Gain for split at x <= 0.2 at level 1 is: "+str(gini_x2_gain))

    #Gini at y1 = 0.4 level 1:
    split_less_y1_ar = 0.4
    split_gre_y1_ar = 0.6
    y1_less_a_area = 0.4
    y1_less_b_area = 0
    y1_less_area = y1_less_a_area + y1_less_b_area
    y1_greater_a_area = (0.6 * 0.5) + (0.2 * 0.3)
    y1_greater_b_area = (0.6 * 0.5) - (0.3 * 0.2)
    y1_greater_area = y1_greater_a_area + y1_greater_b_area
    y1_less_gini = (1 - (((y1_less_a_area/y1_less_area) **2) + ((y1_less_b_area/y1_less_area)**2)))
    y1_greater_gini = (1 - (((y1_greater_a_area/y1_greater_area)**2) + ((y1_greater_b_area/y1_greater_area)**2)))
    y1_gini = ((split_less_y1_ar) * (y1_less_gini)) + ((split_gre_y1_ar) * (y1_greater_gini))
    gini_y1_gain = gini_before_split - y1_gini
    print("6 - Gini for split at y <= 0.4 at level 1 is: "+str(y1_gini))
    print("6 - Gain for split at y <= 0.4 at level 1 is: "+str(gini_y1_gain))

    #Gini at y2 = 0.7 level 1:
    split_less_y2_ar = 0.7
    split_gre_y2_ar = 0.3
    y2_less_a_area = 0.4 + (0.3 * 0.5)
    y2_less_b_area = (0.5 * 0.3)
    y2_less_area = y2_less_a_area + y2_less_b_area
    y2_greater_a_area = (0.3 * 0.5) + (0.2 * 0.3)
    y2_greater_b_area = (0.3 * 0.3)
    y2_greater_area = y2_greater_a_area + y2_greater_b_area
    y2_less_gini = (1 - (((y2_less_a_area/y2_less_area) **2) + ((y2_less_b_area/y2_less_area)**2)))
    y2_greater_gini = (1 - (((y2_greater_a_area/y2_greater_area)**2) + ((y2_greater_b_area/y2_greater_area)**2)))
    y2_gini = ((split_less_y2_ar) * (y2_less_gini)) + ((split_gre_y2_ar) * (y2_greater_gini))
    gini_y2_gain = gini_before_split - y2_gini
    print("6 - Gini for split at y <= 0.7 at level 1 is: "+str(y2_gini))
    print("6 - Gain for split at y <= 0.7 at level 1 is: "+str(gini_y2_gain))

    #Hence, we chose x<=0.5 for the first split.

    # we have the choices of x<=0.2, y<=0.4, y<=0.7 for level-2
    # First gini of the node
    after_split_ar = 0.5
    area_x3_a = (((0.5 * 0.4) + (0.2 * 0.3)) / after_split_ar)
    area_x3_b = (((0.5 * 0.6) - (0.2 * 0.3)) / after_split_ar)
    after_split_gini = (1 - ((area_x3_a**2) + (area_x3_b**2)))
    
    #Gini at x3 = 0.2 at level 2:
    split_less_x3_ar = 0.2/0.5
    split_gre_x3_ar = 0.3/0.5
    x3_less_a_area = (0.2 * 0.4) + (0.2 * 0.3)
    x3_less_b_area = (0.2 * 0.3)
    x3_less_area = x3_less_a_area + x3_less_b_area
    x3_greater_a_area = (0.3 * 0.4) 
    x3_greater_b_area = (0.3 * 0.6)
    x3_greater_area = x3_greater_a_area + x3_greater_b_area
    x3_less_gini = (1 - (((x3_less_a_area/x3_less_area) **2) + ((x3_less_b_area/x3_less_area)**2)))
    x3_greater_gini = (1 - (((x3_greater_a_area/x3_greater_area)**2) + ((x3_greater_b_area/x3_greater_area)**2)))
    x3_gini = ((split_less_x3_ar) * (x3_less_gini)) + ((split_gre_x3_ar) * (x3_greater_gini))
    gini_x3_gain = after_split_gini - x3_gini
    print("6 - Gini for split at x <= 0.2 at level 2 is: "+str(x3_gini))
    print("6 - Gain for split at x <= 0.2 at level 2 is: "+str(gini_x3_gain))

    #Gini at y3 = 0.4 at level 2:
    split_less_y3_ar = 0.2/0.5
    split_gre_y3_ar = 0.3/0.5
    y3_less_a_area = 0.2
    y3_less_b_area = 0
    y3_less_area = y3_less_a_area + y3_less_b_area
    y3_greater_a_area = (0.2 * 0.3)
    y3_greater_b_area = (0.6 * 0.5) - (0.3 * 0.2)
    y3_greater_area = y3_greater_a_area + y3_greater_b_area
    y3_less_gini = (1 - (((y3_less_a_area/y3_less_area) **2) + ((y3_less_b_area/y3_less_area)**2)))
    y3_greater_gini = (1 - (((y3_greater_a_area/y3_greater_area)**2) + ((y3_greater_b_area/y3_greater_area)**2)))
    y3_gini = ((split_less_y3_ar) * (y3_less_gini)) + ((split_gre_y3_ar) * (y3_greater_gini))
    gini_y3_gain = after_split_gini - y3_gini
    print("6 - Gini for split at y <= 0.4 at level 2 is: "+str(y3_gini))
    print("6 - Gain for split at y <= 0.4 at level 2 is: "+str(gini_y3_gain))

    #Gini at y4 = 0.7 at level 2:
    split_less_y4_ar = 0.35/0.5
    split_gre_y4_ar = 0.15/0.5
    y4_less_a_area = (0.4 * 0.5)
    y4_less_b_area = (0.3 * 0.5)
    y4_less_area = y4_less_a_area + y4_less_b_area
    y4_greater_a_area = (0.2 * 0.3)
    y4_greater_b_area = (0.3 * 0.3)
    y4_greater_area = y4_greater_a_area + y4_greater_b_area
    y4_less_gini = (1 - (((y4_less_a_area/y4_less_area) **2) + ((y4_less_b_area/y4_less_area)**2)))
    y4_greater_gini = (1 - (((y4_greater_a_area/y4_greater_area)**2) + ((y4_greater_b_area/y4_greater_area)**2)))
    y4_gini = ((split_less_y4_ar) * (y4_less_gini)) + ((split_gre_y4_ar) * (y4_greater_gini))
    gini_y4_gain = after_split_gini - y4_gini
    print("6 - Gini for split at y <= 0.7 at level 2 is: "+str(y4_gini))
    print("6 - Gain for split at y <= 0.7 at level 2 is: "+str(gini_y4_gain))

    #so from this we select y <= 0.4 for the level 2 split as it has the most gain  
   
    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "B"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    miscls_area = 0.2 * 0.3
    total_area = 1.0
    error_expected = miscls_area/total_area
    print("6 - Expected error rate is: "+str(error_expected))
    answer["b, expected error"] = 0.06

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x <= 0.5")
    x_lesser_l = tree.insert_left("y <= 0.4") 
    tree.insert_right("A")
    x_lesser_l.insert_left("A")
    x_lesser_l.insert_right("B")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.5310044064107188

    #7 Part a:
    #Initial Entropy:
    pos_ex_i = 10
    neg_ex_i = 10
    total_ex_i = pos_ex_i + neg_ex_i
    entropy_before = (-((pos_ex_i/total_ex_i) * u.log2 (pos_ex_i/total_ex_i)) - ((neg_ex_i/total_ex_i) * u.log2 (neg_ex_i/total_ex_i)))
    print ("7(a) - Total entropy before split: " + str(entropy_before))

    # Every node is pure. So, the entropy for splitting by ID would be zero
    info_gain_7a = entropy_before - 0
    print("7(a) - Information gain using ID attribute: " + str(info_gain_7a))

    # 7 Part b:
    #Handedness entropy: we split into left or right handend:
    # Split for left-handedness:
    pos_ex_l = 9
    neg_ex_l = 1
    total_ex_l = pos_ex_l + neg_ex_l
    entropy_left = (-((pos_ex_l/total_ex_l) * u.log2 (pos_ex_l/total_ex_l)) - ((neg_ex_l/total_ex_l) * u.log2 (neg_ex_l/total_ex_l)))
    print ("7(b) - Entropy for left-handed split: " + str(entropy_left))

    # Split for right-handedness:
    pos_ex_r = 1
    neg_ex_r = 9
    total_ex_r = pos_ex_r + neg_ex_r
    entropy_right = (-((pos_ex_r/total_ex_r) * u.log2 (pos_ex_r/total_ex_r)) - ((neg_ex_r/total_ex_r) * u.log2 (neg_ex_r/total_ex_r)))
    print ("7(b) - Entropy for right-handed split: " + str(entropy_right))

    # Information gain for Part b:
    split_left = 10
    split_right = 10
    split_total = split_left + split_right
    info_gain_7b = (entropy_before - (((split_left/split_total) * (entropy_left)) + ((split_right/split_total) * (entropy_right))))
    print("7(b) - Information gain with handedness split is: " + str(info_gain_7b))

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"
    #ID will be selected since it provides more information gain, however this isn't the proper situation as it will result in overfitting

    # answer is a float
    answer["d, gain ratio, ID"] = 0.23137821315975915
    answer["e, gain ratio, Handedness"] = 0.5310044064107188

    # 7 Part d:
    spt_id = 1
    spt_info_id = (-20 * ((spt_id/split_total) * u.log2(spt_id/split_total)))
    print("7(d) - Split info for ID split is: " + str(spt_info_id))
    gain_ratio_id = (info_gain_7a/spt_info_id)
    print("7(d) - Gain ratio for ID split is: " + str(gain_ratio_id))

    # 7 Part e:
    spt_info_handedness = -(((split_left/split_total) * u.log2(split_left/split_total)) + ((split_right/split_total) * u.log2(split_right/split_total)))
    print("7(e) - Split info for handedness split is: " + str(spt_info_handedness))
    gain_ratio_handedness = (info_gain_7b/spt_info_handedness)
    print("7(e) - Gain ratio for handedness split is: " + str(gain_ratio_handedness)) 

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"
    # Handedness has a higher gain ratio than the split with ID

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

