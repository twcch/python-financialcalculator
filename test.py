from datetime import datetime
from dto.claim_benefit_params import ClaimBenefitParams


def main():
    test1()


def test1():
    coverage_start_date = datetime(2020, 1, 1)
    date_of_loss = datetime(2023, 5, 1)

    claim_benefit_params = ClaimBenefitParams()
    claim_benefit_params.set_coverage_start_date(coverage_start_date)
    claim_benefit_params.set_date_of_loss(date_of_loss)

    result = claim_benefit_params.calculate_period_days_for_policy_value_reserve()

    print(result)


if __name__ == "__main__":
    main()
