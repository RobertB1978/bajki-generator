import { describe, it, expect } from "vitest";
import { render } from "@testing-library/react";
import Generate from "../pages/Generate";

describe("Smoke", () => {
  it("renders generator header", () => {
    const { getByText } = render(<Generate />);
    expect(getByText("Generator bajek")).toBeInTheDocument();
  });
});
