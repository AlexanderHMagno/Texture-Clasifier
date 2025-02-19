import gradio as gr


article = """
    <div style='text-align: left; padding: 20px;'>
        <h2 style='margin-bottom: 1rem; color: #333; font-weight: 700;'>How to Use</h2>
        <ul style='padding-left: 20px; font-size: 1rem; color: #555;'>
            <li>Upload or drag-and-drop an image of a material texture</li>
            <li>The model will analyze the texture patterns</li>
            <li>View the predicted material category</li>
        </ul>
    </div>
    """

theme = gr.themes.Base().set(
        body_background_fill="linear-gradient(to right, #f5f5f5, #e8e8e8)",  # Gradient background
        block_background_fill="rgba(255, 255, 255, 0.7)",  # Glass effect
        block_border_width="0px",
        block_radius="12px",  # Rounded corners for sections
        block_shadow="0 4px 8px rgba(0,0,0,0.2)",  # Soft shadow effect
        button_primary_background_fill="#007bff",  # Professional blue button
        button_primary_background_fill_hover="#0056b3",
        button_primary_text_color="#ffffff",
        button_secondary_background_fill="rgba(0,0,0,0.05)",
        button_secondary_background_fill_hover="rgba(0,0,0,0.1)",
        button_secondary_text_color="#333",
        input_background_fill="rgba(255, 255, 255, 0.8)",
        input_border_color="#d1d1d1",
        input_border_width="1px",
        input_shadow="0 2px 4px rgba(0,0,0,0.1)",
        input_radius="6px",
    )

css = """
        .gradio-container {
            max-width: 900px;
            margin: auto;
            padding: 30px;
            background: RGBA(50, 50, 50, 0.2);
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        }

        .image-container {
            background: rgba(0,0,0,0.85);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            height: 250px;
        }

        .image-container img {
            max-width: 100%;
            border-radius: 10px;
            object-fit: cover;
        }

        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #666;
            margin-top: 20px;
        }

        .gradio-button {
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
        }

        .gradio-button.primary {
            background: linear-gradient(135deg, #007bff, #0056b3);
            border: none;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
        }

        .gradio-button.primary:hover {
            background: linear-gradient(135deg, #0056b3, #004094);
            transform: scale(1.05);
        }

        .gradio-button.secondary {
            background: rgba(0, 0, 0, 0.05);
            color: #333;
            border: 1px solid #ccc;
        }

        .gradio-button.secondary:hover {
            background: rgba(0, 0, 0, 0.1);
        }

        label {
            font-size: 0.5rem;
            font-weight: bold;
            color: #222;
            background: black;
            color: white;
            border: none;
        }
    """