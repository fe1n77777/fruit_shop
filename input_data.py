from colorama import Fore, Style
from constants import Constants
import re


class InputData:

  @staticmethod
  def int_input(input_message, field_name, min_value, max_value):
    while True:
      try:
        input_value = input(input_message).strip()
        if input_value.lower() == "cancel":
          print(f"{Fore.LIGHTRED_EX}Operation cancelled.{Style.RESET_ALL}")
          return None
        input_value = int(input_value)
        if input_value <= 0:
          raise ValueError(
              f"{Fore.RED}\"{field_name}\" must be greater than 0.{Style.RESET_ALL}"
          )
        elif input_value < min_value or input_value > max_value:
          raise ValueError(
              f"{Fore.RED}\"{field_name}\" must be between {min_value} and {max_value}.{Style.RESET_ALL}"
          )
        return input_value
      except ValueError as ve:
        print(f"{Fore.RED}{ve}{Style.RESET_ALL}")

  @staticmethod
  def name_input(input_message, field_name, regex, regex_err_message):
    while True:
      try:
        input_value = input(input_message).strip()
        if input_value.lower() == "cancel":
          print(f"{Fore.LIGHTRED_EX}Operation cancelled.{Style.RESET_ALL}")
          return None
        min_length = Constants.MIN_NAME_LENGTH
        max_length = Constants.MAX_NAME_LENGTH

        if not isinstance(input_value, str):
          raise TypeError(
              f"{Fore.RED}\"{field_name}\" must be a string.{Style.RESET_ALL}")

        if len(input_value) < min_length or len(input_value) > max_length:
          raise ValueError(
              f"{Fore.RED}\"{field_name}\" must be between {min_length} and {max_length} characters.{Style.RESET_ALL}"
          )
        if not re.match(regex, input_value):
          raise ValueError(f"{Fore.RED}{regex_err_message}{Style.RESET_ALL}")

        return input_value

      except TypeError as te:
        print(f"{Fore.RED}{te}{Style.RESET_ALL}")
      except ValueError as ve:
        print(f"{Fore.RED}{ve}{Style.RESET_ALL}")

  @staticmethod
  def float_input(input_message, field_name, min_value, max_value):
    while True:
      try:
        input_value = input(input_message).strip()
        if input_value.lower() == "cancel":
          print(f"{Fore.LIGHTRED_EX}Operation cancelled.{Style.RESET_ALL}")
          return None
        input_value = float(input_value)
        if input_value <= 0:
          raise ValueError(
              f"{Fore.RED}\"{field_name}\" must be greater than 0.{Style.RESET_ALL}"
          )
        elif input_value < min_value or input_value > max_value:
          raise ValueError(
              f"{Fore.RED}\"{field_name}\" must be between {min_value} and {max_value}.{Style.RESET_ALL}"
          )
        return input_value
      except ValueError:
        print(
            f"{Fore.RED}Invalid input. Please enter a valid \"{field_name}\".{Style.RESET_ALL}"
        )
