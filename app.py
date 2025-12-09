"""
CISC-121 Searching Algorithm Demo
Linear Search Visualizer 

This app allows the user to enter a list of numbers and a target value.
It then runs Linear Search step-by-step and shows what happens at each step.
"""

import gradio as gr


def parse_number_list(list_str: str): # Convert a comma-separated string like into list of integers. Raise ValueError if parsing fails.

    if not list_str.strip():
        raise ValueError("Please enter at least one number.")

    parts = list_str.split(",")
    numbers = []

    for p in parts:
        p = p.strip()
        if p == "":
            continue
        try:
            n = int(p)
        except ValueError:
            raise ValueError(f"'{p}' is not a valid integer.")
        numbers.append(n)

    if len(numbers) == 0:
        raise ValueError("Please enter at least one valid integer.")

    return numbers


def linear_search_with_steps(arr, target): # Run linear search on list 'arr' and record what happens at each step. Return found/not, index where target found, steps to finding target

    steps = []

    for i, value in enumerate(arr):
        steps.append(
            f"**Step {i + 1}:** Look at index {i}, value = {value}."
        )

        if value == target:
            steps.append(
                f"SUCCESS. The value at index **{i}** equals the target {target}. "
                "Stop searching."
            )
            return True, i, steps
        else:
            steps.append(
                f"{value} is **not** equal to {target}, so move to the next index."
            )

    steps.append(
        f"FAILURE: Reached the end of the list without finding {target}. "
        "Linear search stops here."
    )
    return False, -1, steps


def run_app(list_str, target_str):  # Main function called by the Gradio interface. Parses user input, runs linear search, and returns markdown text describing the result and the steps

    try:
        # Parse the list of numbers
        numbers = parse_number_list(list_str)

        # Parse the target value
        target_str = str(target_str).strip()
        if target_str == "":
            raise ValueError("Please enter a target number to search for.")
        try:
            target = int(target_str)
        except ValueError:
            raise ValueError(f"Target '{target_str}' is not a valid integer.")

        # Run the search
        found, index, steps = linear_search_with_steps(numbers, target)

        # Build markdown output
        output_lines = []

        output_lines.append("## Input")
        output_lines.append(f"- List: `{numbers}`")
        output_lines.append(f"- Target value: `{target}`")
        output_lines.append("")

        output_lines.append("## Result")
        if found:
            output_lines.append(
                f"- SUCCESS: The target **{target}** was found at index **{index}** "
                "(0-based index)."
            )
        else:
            output_lines.append(
                f"- FAILURE: The target **{target}** was **not** found in the list."
            )
        output_lines.append("")

        output_lines.append("## Step-by-step Linear Search")
        for s in steps:
            output_lines.append(f"- {s}")

        return "\n".join(output_lines)

    except ValueError as e:
        # Show user-friendly error messages
        return f" **Input Error:** {e}"


# Gradio user interface definition 

description_text = """
This app demonstrates **Linear Search** on a list of integers.

1. Enter a list of integers separated by commas (e.g., `4, 9, 1, 7`).
2. Enter the target integer you want to search for.
3. Click **Run Search** to see each step of the algorithm.
"""

with gr.Blocks(title="Linear Search Visualizer") as demo:
    gr.Markdown("# Linear Search Visualizer")
    gr.Markdown(description_text)

    with gr.Row():
        list_input = gr.Textbox(
            label="List of integers (comma-separated)",
            placeholder="e.g., 4, 9, 1, 7",
        )
        target_input = gr.Textbox(
            label="Target value to search for",
            placeholder="e.g., 7",
        )

    run_button = gr.Button("Run Search")

    output_markdown = gr.Markdown(label="Search Result")

    run_button.click(
        fn=run_app,
        inputs=[list_input, target_input],
        outputs=output_markdown,
    )

if __name__ == "__main__":
    demo.launch()
