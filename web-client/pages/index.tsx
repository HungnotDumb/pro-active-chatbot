
import { NextPage } from "next";
import React from "react";
import styles from "../styles/Home.module.css";
import { useChatBotResponseMutation } from "../src/generated/graphql";
import Message from "../components/Message/Message";

export interface MessageType {
  user: string;
  message: string;
  time: string;
}
const Home: NextPage = () => {
  const [question, setQuestion] = React.useState("");
  const [askQn, { loading }] = useChatBotResponseMutation();
  const [messages, setMessages] = React.useState<MessageType[]>([]);

  const askQuestion = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!question) return;
    setMessages((prev) => [
      ...prev,
      {
        message: question,
        user: "you",
        time: `${
          String(new Date().getHours()).length < 2
            ? "0" + new Date().getHours().toString()