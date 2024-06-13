import { Button, Text, border } from "@chakra-ui/react"
import { PropsWithChildren } from "react"

type DefaultButtonVariants = "primary" | "secondary"

type DefaultButtonProps = {
  variant?: DefaultButtonVariants
  isSubmit?: boolean
  isDisabled?: boolean
  onClick?: () => void
}

const defaultButtonDisabledStyles = {
  bg: "gray.100",
  color: "gray.300",
  border: "1px solid",
  borderColor: "gray.200",
  cursor: "not-allowed",
}

const defaultButtonVariantStyles = {
  primary: {
    bg: "green.800",
    color: "white",
    _hover: {
      bg: "green.700",
      _disabled: defaultButtonDisabledStyles,
    },
    _disabled: defaultButtonDisabledStyles,
  },
  secondary: {
    bg: "gray.100",
    color: "gray.700",
    border: "1px solid",
    borderColor: "gray.800",
    _hover: {
      bg: "gray.50",
      _disabled: defaultButtonDisabledStyles,
    },
    _disabled: defaultButtonDisabledStyles,
  },
}

const defaultButtonStyles = {
  px: "12px",
  height: "32px",
  borderRadius: "4px",
}

const DefaultButton: React.FC<PropsWithChildren<DefaultButtonProps>> = ({
  children,
  variant,
  isSubmit,
  isDisabled,
  onClick,
}) => {
  if (isSubmit === undefined) {
    isSubmit = false
  }
  if (variant === undefined) {
    variant = "primary"
  }
  if (isDisabled === undefined) {
    isDisabled = false
  }

  return (
    <Button
      type={isSubmit ? "submit" : "button"}
      sx={{ ...defaultButtonVariantStyles[variant], ...defaultButtonStyles }}
      isDisabled={isDisabled}
      onClick={onClick}
    >
      <Text size="md" fontWeight="bold">
        {children}
      </Text>
    </Button>
  )
}

export default DefaultButton
