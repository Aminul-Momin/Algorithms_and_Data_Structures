""" Compute a salary threshold. - [EPI:13.12]. """


def find_salary_cap(target_payroll, current_salaries):

    current_salaries.sort()
    unadjusted_salary_sum = 0.0
    for i, current_salary in enumerate(current_salaries):
        adjusted_people = len(current_salaries) - i
        adjusted_salary_sum = current_salary * adjusted_people
        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people
        unadjusted_salary_sum += current_salary
    # No solution, since target_payroll > existing payroll.
    return -1.0


def main():
    pass


if __name__ == '__main__':
    main()