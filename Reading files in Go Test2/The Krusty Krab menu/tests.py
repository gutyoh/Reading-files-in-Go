import os

from hstest import StageTest, CheckResult, WrongAnswer, TestCase

inputs = [
    "Krabby Pattie $2.00\nKrusty Combo $3.99\nKrusty Deluxe $3.00\nSeaweed Salad $1.50\nCoral Bits $1.95"
]

# Create new file "galley_grub.txt"
with open("galley_grub.txt", "w") as f:
    for line in inputs:
        f.write(line)

FILENAME = "galley_grub.txt"


class TestAdmissionProcedure(StageTest):
    def generate(self):
        return [TestCase(stdin=[test], attach=[test]) for test in inputs]

    def check(self, reply: str, attach: list):
        if not os.path.exists(FILENAME):
            raise WrongAnswer(f"Cannot find file {FILENAME}")

        with open(FILENAME, "r") as f:
            content = f.read().strip()
            if content != attach[0]:
                raise WrongAnswer(
                    f'Invalid content of {FILENAME} file, got "{content}" want "{attach[0]}"'
                )

        return CheckResult.correct()


if __name__ == '__main__':
    TestAdmissionProcedure().run_tests()
