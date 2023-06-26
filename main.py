def main():
    ##################################################
    # Complete your code here
    ##################################################
    original_str = "Python Programming"
    sub1 = original_str[0:6]
    sub2 = original_str[7:18] # or sub2 = original_str[7:]
    merged_str = sub2 + " " + sub1

    print(sub2)
    print(sub1)
    print(merged_str)

if __name__ == '__main__':
    main()
