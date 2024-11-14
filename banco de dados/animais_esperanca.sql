-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 14/11/2024 às 20:07
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `animais_esperanca`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `animais`
--

CREATE TABLE `animais` (
  `id_animais` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `raca` varchar(50) NOT NULL,
  `especie` varchar(50) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `idade` varchar(2) NOT NULL,
  `localResgatado` varchar(50) NOT NULL,
  `resgatador` varchar(50) NOT NULL,
  `abrigo` varchar(50) NOT NULL,
  `fk_tutores` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `animais`
--

INSERT INTO `animais` (`id_animais`, `nome`, `raca`, `especie`, `genero`, `idade`, `localResgatado`, `resgatador`, `abrigo`, `fk_tutores`) VALUES
(2, 'andrezitos', 'humana', 'youtuber', 'M', '27', 'santos', 'deus', 'santos', 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tutores`
--

CREATE TABLE `tutores` (
  `id_tutores` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `telefone` varchar(11) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `senha` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tutores`
--

INSERT INTO `tutores` (`id_tutores`, `nome`, `telefone`, `endereco`, `email`, `senha`) VALUES
(1, 'NICOLAS', '984109830', 'AV NESTOR JARDIM FILHO', 'NICOLAS@GMAIL.COM', '1234'),
(3, 'nicolas', '984109830', 'av nestor jardim filho', 'nicolas@gmail.com', 'diovani'),
(4, 'nicola', '112454323', 'av bla bla bla', 'gmail.com', 'senhasenha'),
(5, 'lucas sol', '51965452354', 'av lusitana 564', 'lucassolito@gmail.com', 'bianca123'),
(7, 'anderson', '5198341234', 'av garfield', 'junior@gmail.com', '1234'),
(8, 'joao', '54123452312', 'av tiago', 'fabio@gmail.com', 'pokemon'),
(10, 'nicolas', 'a', 'a', 'a', 'a'),
(11, '& \"C:/Users/di8va/OneDrive/Doc', '981234512', 'av bla bla bla', 'sla@gmail.com', '12345');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `animais`
--
ALTER TABLE `animais`
  ADD PRIMARY KEY (`id_animais`),
  ADD KEY `fk_tutores` (`fk_tutores`);

--
-- Índices de tabela `tutores`
--
ALTER TABLE `tutores`
  ADD PRIMARY KEY (`id_tutores`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `animais`
--
ALTER TABLE `animais`
  MODIFY `id_animais` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `tutores`
--
ALTER TABLE `tutores`
  MODIFY `id_tutores` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `animais`
--
ALTER TABLE `animais`
  ADD CONSTRAINT `fk_tutores` FOREIGN KEY (`fk_tutores`) REFERENCES `tutores` (`id_tutores`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
