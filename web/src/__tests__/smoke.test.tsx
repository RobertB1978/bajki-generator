import { describe, it, expect } from "vitest";
import { render } from "@testing-library/react";
import App from "../pages/App";

describe("Smoke", () => {
  it("renders generator header", () => {
    const { getByText } = render(<App />);
    expect(getByText("Bajki Generator")).toBeInTheDocument();
  });
});
