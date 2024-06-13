import DefaultButton from "@/components/button/default-button"
import {
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  InputRightElement,
  Text,
  VStack,
} from "@chakra-ui/react"
import { useState } from "react"
import { FaEye, FaEyeSlash } from "react-icons/fa6"

const getServerSideProps = async () => {
  return {
    props: {
      title: "Login",
      description: "Login to your account",
      authNeeded: false,
    },
  }
}

const LoginPage: React.FC = () => {
  const [showPassword, setShowPassword] = useState(false)
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    console.log("submitted")
  }
  return (
    <VStack>
      <form onSubmit={handleSubmit}>
        <FormControl>
          <FormLabel>Email</FormLabel>
          <Input type="email" />
        </FormControl>
        <FormControl>
          <FormLabel>Password</FormLabel>
          <InputGroup>
            <Input type={showPassword ? "text" : "password"} />
            <InputRightElement>
              <Text
                as={showPassword ? FaEye : FaEyeSlash}
                onClick={() => {
                  setShowPassword(!showPassword)
                }}
              />
            </InputRightElement>
          </InputGroup>
        </FormControl>
        <DefaultButton isSubmit={true}>Login</DefaultButton>
      </form>
    </VStack>
  )
}

export default LoginPage
