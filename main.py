from controller.log_controller import LogController

from controller.date_controller import DateController
from controller.calculator_controller import CalculatorController


def main():
    set_log_controller()
    call_calculator_controller()
    call_date_controller()


def call_calculator_controller():
    calculator_controller = CalculatorController()
    calculator_controller.compute_discount()


def call_date_controller():
    date_controller = DateController()
    date_controller.compute_adjust_date()


def set_log_controller():  # 配置 log 控制器
    log_path = "./log/logger.log"
    LogController(log_path)


if __name__ == "__main__":
    main()
